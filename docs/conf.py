# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Project Name'
copyright = '2024, Aidemy Inc.'
author = 'Aidemy Inc.'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

from pathlib import Path
import sys

sys.path.insert(0, str(Path("../")))

extensions = [
    "sphinx.ext.autodoc", 
    "sphinx.ext.napoleon", 
    "sphinx_rtd_theme",
    'sphinxcontrib.mermaid',
    'sphinxcontrib.plantuml',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_default_options = {
    'private-members': True,  # 非公開メンバーを含める
    # 'special-members': True,  # "__special__"メソッドを含める
    'undoc-members': True,    # ドキュメントがないメンバーも含める
    'exclude-members': '__weakref__'  # 特定のメンバーを除外する
}
autodoc_member_order = 'bysource'

plantuml = 'java -jar /usr/share/plantuml/plantuml.jar'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']