from zope.interface import implementer
from sqlalchemy import (
    Column,
    String,
    Unicode,
    Integer,
    Boolean,
    ForeignKey,
    UniqueConstraint,
)
from clld import interfaces
from clld.db.meta import Base, CustomModelMixin
from clld.db.models import common
from clld_ipachart_plugin.models import InventoryMixin
from clld_glottologfamily_plugin.models import HasFamilyMixin


#-----------------------------------------------------------------------------
# specialized common mapper classes
#-----------------------------------------------------------------------------

@implementer(interfaces.ILanguage)
class Variety(CustomModelMixin, common.Language, HasFamilyMixin, InventoryMixin):
    pk = Column(Integer, ForeignKey('language.pk'), primary_key=True)
    glottocode = Column(Unicode)

    order = Column(Integer)
    number = Column(Unicode)
    family_in_source = Column(Unicode)


@implementer(interfaces.IParameter)
class Concept(CustomModelMixin, common.Parameter):
    pk = Column(Integer, ForeignKey('parameter.pk'), primary_key=True)
    concepticon_id = Column(Unicode)
    pages = Column(Unicode)

    @property
    def scans(self):
        for number in self.pages.split('-'):
            try:
                number = int(number)
                yield 'https://dsal.uchicago.edu/books/lsi/images/lsi-v1-2-{}.jpg'.format(
                    str(number + 42).rjust(3, '0'))
            except:
                pass


@implementer(interfaces.IValue)
class Form(CustomModelMixin, common.Value):
    pk = Column(Integer, ForeignKey('value.pk'), primary_key=True)
    segments = Column(Unicode)
