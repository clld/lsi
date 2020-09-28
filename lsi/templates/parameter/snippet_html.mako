<div id="scans-container">
    % for scan in ctx.scans:
        <div class="span6">
            <a href="${scan}" target="_blank">
                <img src="${scan}" alt="scan"/>
            </a>
        </div>
    % endfor
</div>