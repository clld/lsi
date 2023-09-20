from sqlalchemy.orm import joinedload
from clld.web import datatables
from clld.web.datatables.base import LinkCol, Col, LinkToMapCol, DetailsRowLinkCol
from clld.web.datatables.value import Values
from clld.web.datatables.parameter import Parameters
from clld.web.util import concepticon
from clld.db.models import common

from clld_glottologfamily_plugin.models import Family
from clld_glottologfamily_plugin.datatables import FamilyCol


from lsi import models


class Words(Values):
    def base_query(self, query):
        query = Values.base_query(self, query)
        if self.parameter:
            query = query.outerjoin(models.Variety.family)

        return query

    def col_defs(self):
        if self.parameter:
            return [
                LinkCol(
                    self,
                    'language',
                    model_col=common.Language.name,
                    get_object=lambda i: i.valueset.language),
                FamilyCol(
                    self,
                    'family',
                    models.Variety,
                    get_object=lambda i: i.valueset.language),
                #
                # Add
                # - language family
                # - ID order
                #
                Col(self, 'name', sTitle='Orthography'),
                Col(self, 'description', sTitle='IPA'),
                Col(self, 'segments', model_col=models.Form.segments),
                LinkToMapCol(self, 'm', get_object=lambda i: i.valueset.language),
            ]

        if self.language:
            return [
                LinkCol(self,
                        'parameter',
                        sTitle=self.req.translate('Parameter'),
                        model_col=common.Parameter.name,
                        get_object=lambda i: i.valueset.parameter),
                Col(self, 'name', sTitle='Orthography'),
                Col(self, 'description', sTitle='IPA'),
                Col(self, 'segments', model_col=models.Form.segments),
            ]

        return [
            Col(self, 'name', sTitle='Orthography'),
            Col(self, 'description', sTitle='IPA'),
            Col(self, 'segments', model_col=models.Form.segments),
        ]


class NumberCol(Col):
    def order(self):
        return models.Variety.order


class Languages(datatables.Languages):
    def base_query(self, query):
        return query.outerjoin(Family).options(joinedload(models.Variety.family)).distinct()

    def col_defs(self):
        return [
            NumberCol(self, 'number', input_size='mini', sClass='right'),
            LinkCol(self, 'name'),
            FamilyCol(self, 'Family', models.Variety),
            Col(self, 'family_in_source', model_col=models.Variety.family_in_source),
            Col(self,
                'latitude',
                sDescription='<small>The geographic latitude</small>'),
            Col(self,
                'longitude',
                sDescription='<small>The geographic longitude</small>'),
            LinkToMapCol(self, 'm'),
        ]


class ConcepticonCol(Col):
    def format(self, item):
        if not item.concepticon_id:
            return ''
        return concepticon.link(self.dt.req, id=item.concepticon_id, label=item.description)


class Vocabulary(Parameters):
    def col_defs(self):
        return [
            LinkCol(self, 'name'),
            ConcepticonCol(self, 'description', sTitle='Concepticon'),
            DetailsRowLinkCol(self, 'source', button_text='Source'),
        ]


def includeme(config):
    """register custom datatables"""

    config.register_datatable('parameters', Vocabulary)
    config.register_datatable('values', Words)
    config.register_datatable('languages', Languages)
