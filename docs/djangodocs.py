"""
Sphinx plugin for Django documentation.
"""

import json
import os
import re

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.statemachine import ViewList
from sphinx import addnodes
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.directives import CodeBlock
from sphinx.domains.std import Cmdoption
from sphinx.errors import ExtensionError
from sphinx.util import logging
from sphinx.util.console import bold
from sphinx.writers.html import HTMLTranslator