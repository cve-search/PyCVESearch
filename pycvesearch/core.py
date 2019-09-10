#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from urllib.parse import urljoin


class CVESearch(object):

    def __init__(self, base_url='https://cve.circl.lu', proxies=None,
                 timeout=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.proxies = proxies
        self.session.headers.update({
            'content-type': 'application/json',
            'User-Agent': 'PyCVESearch - python wrapper'})
        self.timeout = timeout

    def _http_get(self, api_call, query=None):
        return self.session.get(
            urljoin(
                self.base_url,
                '/'.join(filter(None, ('api', str(api_call), str(query))))),
            timeout=self.timeout)

    def browse(self, param=None):
        """ browse() returns a dict containing all the vendors browse(vendor)
            returns a dict containing all the products associated to a vendor
        """
        data = self._http_get('browse', query=param)
        return data.json()

    def search(self, param):
        """ search() returns a dict containing all the vulnerabilities per
            vendor and a specific product
        """
        data = self._http_get('search', query=param)
        return data.json()

    def id(self, param):
        """ id() returns a dict containing a specific CVE ID """
        data = self._http_get('cve', query=param)
        return data.json()

    def last(self, param=None):
        """ last() returns a dict containing the last 30 CVEs including CAPEC,
            CWE and CPE expansions
        """
        data = self._http_get('last', query=param)
        return data.json()

    def dbinfo(self):
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

    def cvefor(self, param):
        """ cvefor() returns a dict containing the CVE's for a given CPE ID
        """
        data = self._http_get('cvefor', query=param)
        return data.json()
