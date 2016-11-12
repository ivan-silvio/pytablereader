# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import absolute_import

from ..error import LoaderNotFoundError
from ..factory import TableUrlLoaderFactory
from ._base import TableLoaderManager


class TableUrlLoader(TableLoaderManager):
    """
    Loader class to loading tables from URL.

    :param str url: URL to load.
    :param str format_name: Data format name to load.
        Supported formats are:
            * ``"csv"``
            * ``"excel"``
            * ``"html"``
            * ``"json"``
            * ``"markdown"``
            * ``"mediawiki"``
    :param dict proxies: http/https proxy information.

        .. seealso::
            - `requests proxies <http://requests-docs-ja.readthedocs.io/en/latest/user/advanced/#proxies>`__

    :raises pytablereader.LoaderNotFoundError:
        If appropriate loader not found to loading the URL.
    :raises pytablereader.HTTPError:
        If loader received an HTTP error when access to the URL.
    """

    def __init__(self, url, format_name=None, proxies=None):
        loader_factory = TableUrlLoaderFactory(url, proxies)

        try:
            loader = loader_factory.create_from_format_name(format_name)
        except (LoaderNotFoundError, ValueError):
            loader = loader_factory.create_from_path()

        super(TableUrlLoader, self).__init__(loader)
