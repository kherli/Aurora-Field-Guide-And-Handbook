# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Handbook'
copyright = '2024, ARCTICS'
author = 'ARCTICS'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
extensions = ["sphinx.ext.imgmath", "sphinx_wagtail_theme", "sphinxcontrib.bibtex"]
bibtex_bibfiles = ["../../references.bib"]
html_theme = "sphinx_wagtail_theme"
html_static_path = ["_static"]
master_doc = "index"
html_extra_path = ["_static"]
numfig = True
numfig_secnum_depth = 3
html_title = "ARCTICS Aurora Field Guide And Handbook"
project = "ARCTICS Aurora Field Guide And Handbook"
html_title = "ARCTICS Aurora Field Guide And Handbook"
html_short_title = "ARCTICS Aurora Guides"
html_context = {
    "display_github": True,
    "github_user": "kherli",
    "github_repo": "Aurora-Field-Guide-And-Handbook",
    "github_version": "gh-pages",
    "conf_py_path": "/docs/source/", 
}
html_theme_options = {
    "site_name": "ARCTICS Aurora Field Guide And Handbook",
    "github_url": "https://github.com/kherli/Aurora-Field-Guide-And-Handbook/tree/gh-pages/docs/source/",
    "title": "ARCTICS Aurora Field Guide And Handbook",
    "breadcrumb_separator": ">",
    "breadcrumb_home_label": "Home",
}
