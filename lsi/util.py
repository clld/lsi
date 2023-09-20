from clld.web.util import concepticon
from clld.web.util import glottolog


def language_detail_html(context=None, request=None, **kw):
    return context.render_inventory(request=request)
