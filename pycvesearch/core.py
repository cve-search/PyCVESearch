#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pkg_resources

from typing import Optional, Dict, MutableMapping
from urllib.parse import urljoin

import requests


class CVESearch(object):

    def __init__(self, base_url: str, proxies: MutableMapping[str, str]={}, timeout: Optional[int]=None,
                 verify=True, useragent: Optional[str]=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.proxies = proxies
        self.session.headers.update({
            'content-type': 'application/json',
            'User-Agent': useragent if useragent else f'PyCVESearch / {pkg_resources.get_distribution("pycvesearch").version}'})
        self.timeout = timeout
        self.verify = verify

    def _http_get(self, api_call, query=None):
        if query is None:
            url = urljoin(self.base_url, f'api/{api_call}')
        else:
            url = urljoin(self.base_url, f'api/{api_call}/{query}')
        return self.session.get(url, timeout=self.timeout, verify=self.verify)

    def browse(self, param=None) -> Dict:
        """ browse() returns a dict containing all the vendors browse(vendor)
            returns a dict containing all the products associated to a vendor
        """
        data = self._http_get('browse', query=param)
        return data.json()

    def search(self, param) -> Dict:
        """ search() returns a dict containing all the vulnerabilities per
            vendor and a specific product
        """
        data = self._http_get('search', query=param)
        return data.json()

    def id(self, param) -> Dict:
        """ id() returns a dict containing a specific CVE ID """
        data = self._http_get('cve', query=param)
        return data.json()

    def last(self, param=None) -> Dict:
        """ last() returns a dict containing the last 30 CVEs including CAPEC,
            CWE and CPE expansions
        """
        data = self._http_get('last', query=param)
        return data.json()

    def dbinfo(self) -> Dict:
        """ dbinfo() returns a dict containing more information about
            the current databases in use and when it was updated
        """
        data = self._http_get('dbInfo')
        return data.json()

    def cpe22(self, param):
        """ cpe22() returns a string containing the cpe2.2 ID of a cpe2.3 input
        """
        data = self._http_get('cpe2.2', query=param)
        return data

    def cpe23(self, param):
        """ cpe23() returns a string containing the cpe2.3 ID of a cpe2.2 input
        """
        data = self._http_get('cpe2.3', query=param)
        return data

    def cvefor(self, param) -> Dict:
        """ cvefor() returns a dict containing the CVE's for a given CPE ID
        """
        data = self._http_get('cvefor', query=param)
        return data.json()
