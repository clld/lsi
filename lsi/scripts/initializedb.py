import itertools
import collections

from nameparser import HumanName
from pyclts import CLTS
from pycldf import Sources
from clldutils.misc import nfilter, slug
from clldutils.color import qualitative_colors
from clld.cliutil import Data, bibtex2source
from clld.db.meta import DBSession
from clld.db.models import common
from clld.lib import bibtex

from clld_glottologfamily_plugin.util import load_families


import lsi
from lsi import models


def iteritems(cldf, t, *cols):
    cmap = {cldf[t, col].name: col for col in cols}
    for item in cldf[t]:
        for k, v in cmap.items():
            item[v] = item[k]
        yield item


def main(args):
    assert args.glottolog, 'The --glottolog option is required!'

    clts = CLTS(input('Path to cldf-clts/clts:') or '../../cldf-clts/clts')
    data = Data()
    ds = data.add(
        common.Dataset,
        lsi.__name__,
        id=lsi.__name__,
        name='The Comparative Vocabularies of the "Linguistic Survey of India" Online',
        domain='lsi.clld.org',
        publisher_name="Max Planck Institute for the Science of Human History",
        publisher_place="Jena",
        publisher_url="http://www.shh.mpg.de",
        license="http://creativecommons.org/licenses/by/4.0/",
        jsondata={
            'license_icon': 'cc-by.png',
            'license_name': 'Creative Commons Attribution 4.0 International License'},

    )

    for i, name in enumerate(['Taraka Rama', 'Robert Forkel', 'Johann-Mattis List']):
        common.Editor(
            dataset=ds,
            ord=i,
            contributor=common.Contributor(id=slug(HumanName(name).last), name=name)
        )

    contrib = data.add(
        common.Contribution,
        None,
        id='cldf',
        name=args.cldf.properties.get('dc:title'),
        description=args.cldf.properties.get('dc:bibliographicCitation'),
    )

    for lang in iteritems(args.cldf, 'LanguageTable', 'id', 'glottocode', 'name', 'latitude', 'longitude'):
        data.add(
            models.Variety,
            lang['id'],
            id=lang['id'],
            name=lang['name'],
            latitude=lang['latitude'],
            longitude=lang['longitude'],
            glottocode=lang['glottocode'],
            order=int(lang['Order']),
            number=lang['NumberInSource'],
            family_in_source=lang['FamilyInSource'],
        )

    for rec in bibtex.Database.from_file(args.cldf.bibpath):
        data.add(common.Source, rec.id, _obj=bibtex2source(rec))

    refs = collections.defaultdict(list)


    for param in iteritems(args.cldf, 'ParameterTable', 'id', 'concepticonReference', 'name'):
        data.add(
            models.Concept,
            param['id'],
            id=param['id'],
            name='{} [{}]'.format(param['name'], param['id']),
            pages=param['PageNumber'],
        )

    inventories = collections.defaultdict(set)
    for form in iteritems(args.cldf, 'FormTable', 'id', 'form', 'languageReference', 'parameterReference', 'source'):
        inventories[form['languageReference']] = inventories[form['languageReference']].union(form['Segments'])
        vsid = (form['languageReference'], form['parameterReference'])
        vs = data['ValueSet'].get(vsid)
        if not vs:
            vs = data.add(
                common.ValueSet,
                vsid,
                id='-'.join(vsid),
                language=data['Variety'][form['languageReference']],
                parameter=data['Concept'][form['parameterReference']],
                contribution=contrib,
            )
        for ref in form.get('source', []):
            sid, pages = Sources.parse(ref)
            refs[(vsid, sid)].append(pages)
        data.add(
            common.Value,
            form['id'],
            id=form['id'],
            name=form['form'],
            valueset=vs,
        )
    for lid, inv in inventories.items():
        inv = [clts.bipa[c] for c in inv]
        data['Variety'][lid].update_jsondata(
            inventory=[(str(c), c.name) for c in inv if hasattr(c, 'name')])

    for (vsid, sid), pages in refs.items():
        DBSession.add(common.ValueSetReference(
            valueset=data['ValueSet'][vsid],
            source=data['Source'][sid],
            description='; '.join(nfilter(pages))
        ))
    load_families(
        Data(),
        [(l.glottocode, l) for l in data['Variety'].values()],
        glottolog_repos=args.glottolog,
        isolates_icon='tcccccc',
        strict=False,
    )



def prime_cache(args):
    """If data needs to be denormalized for lookup, do that here.
    This procedure should be separate from the db initialization, because
    it will have to be run periodically whenever data has been updated.
    """
