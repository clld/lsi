from pathlib import Path

from clld.web.assets import environment

import lsi


environment.append_path(
    Path(lsi.__file__).parent.joinpath('static').as_posix(),
    url='/lsi:static/')
environment.load_path = list(reversed(environment.load_path))
