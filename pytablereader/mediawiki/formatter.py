# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import absolute_import, unicode_literals

from ..error import PypandocImportError
from ..html.formatter import HtmlTableFormatter


class MediaWikiTableFormatter(HtmlTableFormatter):
    def __init__(self, source_data):
        try:
            import pypandoc
        except ImportError as e:
            # pypandoc package may do not installed in the system since the package is
            # an optional dependency
            raise PypandocImportError(e)

        super(MediaWikiTableFormatter, self).__init__(
            pypandoc.convert_text(source_data, "html", format="mediawiki")
        )
