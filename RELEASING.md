# Releasing lsi

- Install the app:
  ```shell
  git clone https://github.com/clld/lsi
  cd lsi/
  pip install -e .[test]
  ```
- create a release of the lexibank dataset
- import the data into the clld app db running
  ```shell
  clld initdb development.ini --cldf ../../lsi/lsi-cldf/cldf/cldf-metadata.json --glottolog ../../glottolog/glottolog
  ```

