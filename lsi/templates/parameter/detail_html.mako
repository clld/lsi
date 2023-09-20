<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "parameters" %>
<%block name="title">${_('Parameter')} ${ctx.name}</%block>

<ul class="nav nav-pills" style="float: right">
    <li class="">
        <a href="#map-container">
            <img src="${req.static_url('lsi:static/Map_Icon.png')}"
                 width="35">
            Map
        </a>
    </li>
    <li class="">
        <a href="#table-container">
            <img src="${req.static_url('lsi:static/Table_Icon.png')}"
                 width="35">
            Table
        </a>
    </li>
    <li class="">
        <a href="#scans-container">
            <img src="${req.static_url('lsi:static/Book_Icon.png')}"
                 width="35">
            Book
        </a>
    </li>
</ul>


<h2>${_('Parameter')} ${ctx.name}</h2>

% if ctx.concepticon_id:
    <p>
        Related concept set in Concepticon:
        ${u.concepticon.link(req, ctx.concepticon_id, label=ctx.description)}
    </p>
% endif
<p>
    Corresponding book pages at DSAL:
    ${h.external_link(ctx.dsal_url)}
</p>

<div style="clear: both" id="map-container">
    <h4 style="float: right">
        <a href="#top" title="go to top of the page" style="vertical-align: bottom">&#x21eb;</a>
    </h4>
</div>
% if map_ or request.map:
${(map_ or request.map).render()}
% endif

<div id="table-container">
    <h4 style="float: right">
        <a href="#top" title="go to top of the page" style="vertical-align: bottom">&#x21eb;</a>
    </h4>
    ${request.get_datatable('values', h.models.Value, parameter=ctx).render()}
</div>

<div id="scans-container">
    <h4 style="float: right">
        <a href="#top" title="go to top of the page" style="vertical-align: bottom">&#x21eb;</a>
    </h4>
    <div style="clear: both"/>
    % for scan in ctx.scans:
        <div class="span6">
            <a href="${scan}" target="_blank">
                <img src="${scan}"/>
            </a>
        </div>
    % endfor
</div>