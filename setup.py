from setuptools import setup


setup(
    name='ermahgerd',
    packages=['ermahgerd'],
    include_package_data=True,
    install_requires=[
        'flask',
        'nltk',
        'peewee',
        'psycopg2'
    ]
)
