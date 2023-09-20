<%inherit file="home_comp.mako"/>
<%namespace name="util" file="util.mako"/>

<h3>${_('Downloads')}</h3>

${util.dataset_download(label=req.dataset.id.upper())}

