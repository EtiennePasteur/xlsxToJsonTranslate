from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='xlsxToJsonTranslate',
    version='0.1.3',
    description='Convert xlsx file to a json object. Build for i18n angular apps',
    long_description=long_description,
    long_description_content_type="text/markdown",
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
        'xlsxToJsonTranslate',
    ],
    install_requires=[
        "unflatten~=0.1",
        "deepmerge~=0.1.0",
        "xlrd~=1.2.0",
        "simplejson~=3.17.0"
    ],
)
