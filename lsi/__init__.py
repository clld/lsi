from pyramid.config import Configurator

from clld_glottologfamily_plugin import util
from clld_glottologfamily_plugin.util import ISOLATES_ICON

from clld.interfaces import IMapMarker, IValueSet, IValue, IDomainElement
from clldutils.svg import pie, icon, data_url

# we must make sure custom models are known at database initialization!
from lsi import models


_ = lambda s: s
_('Parameters')
_('Parameter')


class LanguageByFamilyMapMarker(util.LanguageByFamilyMapMarker):
    def __call__(self, ctx, req):
    
        if IValueSet.providedBy(ctx):
            if ctx.language.family:
                return data_url(icon(ctx.language.family.jsondata['icon']))
            return data_url(icon(req.registry.settings.get('clld.isolates_icon', ISOLATES_ICON)))
    
        return super(LanguageByFamilyMapMarker, self).__call__(ctx, req)



def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings.update(**{'clld.isolates_icon': 'dff6600'})
    config = Configurator(settings=settings)
    config.include('clld.web.app')

    config.include('clldmpg')


    config.registry.registerUtility(LanguageByFamilyMapMarker(), IMapMarker)

    return config.make_wsgi_app()
