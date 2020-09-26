<%inherit file="app.mako"/>

##
## define app-level blocks:
##
<%block name="brand">
    <a class="brand" href="${request.route_url('dataset')}"
       title="The Coparative Vocabularies of the Linguistic Survey of India Online"
       style="padding-top: 0px; padding-bottom: 0px; padding-right: 0px; padding-left: 0px;">
        <img src="${request.static_url('lsi:static/logo.png')}" width="50"/>
    </a>
</%block>

${next.body()}
