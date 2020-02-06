from setuptools import setup

setup(
    name='xlsxToJsonTranslate',
    version='0.1.0',
    description='Convert xlsx file to a json object. Build for i18n angular apps',
    long_description=open('README.rst', 'rt', encoding='utf-8').read(),
    url='https://github.com/EtiennePasteur/xlsxToJsonTranslate',
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords="json csv xls xlsx translate i18n angular",
    author="Etienne Pasteur",
    author_email="me@etiennepasteur.com",
    zip_safe=True,
    scripts=[
        'xlsxToJsonTranslate.py',
    ],
    install_requires=[
        "unflatten~=0.1",
        "deepmerge~=0.1.0",
        "xlrd~=1.2.0",
    ],
)
