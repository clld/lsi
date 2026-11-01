# Releasing lsi

Install the app:
```shell
git clone --branch v1.1 --depth 1 https://github.com/lexibank/lsi lsi-cldf
git clone --branch v5.3 --depth 1 https://github.com/glottolog/glottolog
git clone --branch v2.3.1 --depth 1 https://github.com/cldf-clts/clts
git clone https://github.com/clld/lsi
cd lsi/
pip install -e .[test]
```

import the data into the clld app db running
```shell
clld initdb development.ini --cldf ../lsi-cldf/cldf/cldf-metadata.json --glottolog ../glottolog
```

```shell
pytest
```

Store the tested requirements:
```shell
pip freeze > requirements.txt
```

Store a db dump:
```shell
pg_dump -xO --compress gzip:9 lsi > lsi.sql.gz
```

