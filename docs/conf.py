# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys
import os
import sphinx_rtd_theme


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PikaPython_VMG0'
copyright = '2024, VeriMake_Edwin'
author = 'VeriMake_Edwin'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = [
#]
extensions = ['recommonmark','sphinx_markdown_tables','sphinx_rtd_theme']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'
master_doc = "index"
source_encoding = "utf-8-sig"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

