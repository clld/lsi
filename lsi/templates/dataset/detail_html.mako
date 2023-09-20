<%inherit file="../home_comp.mako"/>

<%def name="sidebar()">
    <div class="well">
        <h3>Cite as</h3>
        <blockquote>
            Grierson, George Abraham. (2023). CLDF dataset derived from Grierson's "Linguistic Survey of India" from 1928 (v1.0) [Data set]. Zenodo. <a href="https://doi.org/10.5281/zenodo.8361936">https://doi.org/10.5281/zenodo.8361936</a>
        </blockquote>
    </div>
</%def>

<h2>The Comparative Vocabularies of the "Linguistic Survey of India" Online</h2>

<p>
    This ${h.external_link('https://github.com/clld', label='clld')} web application serves the
    ${h.external_link('https://github.com/cldf/cldf/tree/master/modules/Wordlist', label='CLDF Wordlist')}
    derived from the comparative vocabularies of Grierson's "Linguistic Survey of India".
    See <a href="download">the download page</a> for details about how to access the data.
</p>

<div style="text-align: center">
    <iframe src="https://dsal.uchicago.edu/books/lsi/lsi.php?volume=1-2&pages=381#page/1/mode/1up" width="560" height="384" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen></iframe>
</div>
