from setuptools import setup, find_packages


setup(
    name='lsi',
    version='0.0',
    description='lsi',
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'clld>=9.2.2',
        'clldmpg',
        'clld-glottologfamily-plugin>=4.0',
        'clld-ipachart-plugin>=0.2',
        'pyglottolog',
        'pyclts>=2.1'
        'clldmpg',
],
extras_require={
        'dev': ['flake8', 'waitress'],
        'test': [
            'psycopg2',
            'pytest>=5.4',
            'pytest-clld',
            'pytest-mock',
            'pytest-cov',
            'pytest-env',
            'coverage>=4.2',
            'selenium',
            'zope.component>=3.11.0',
        ],
    },
    test_suite="lsi",
    entry_points="""\
    [paste.app_factory]
    main = lsi:main
""")
