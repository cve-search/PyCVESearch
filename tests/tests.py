#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from pycvesearch import CVESearch


class TestPyCVESearch(unittest.TestCase):

    def setUp(self):
        self.cve = CVESearch()

    def test_browse(self):
        self.cve.browse('microsoft')

    def test_search(self):
        self.cve.search('microsoft/office')

    def test_id(self):
        self.cve.id('CVE-2014-0160')

    def test_last(self):
        self.cve.last()

    def test_last_50(self):
        self.cve.last(50)

    def test_dbinfo(self):
        self.cve.dbinfo()

    def test_cpe22(self):
        self.cve.cpe22('cpe:2.3:a:microsoft:office:2011:-:mac')

    def test_cpe23(self):
        self.cve.cpe23('cpe/a:microsoft:office:2011:-:mac')

    def test_cvefor(self):
        self.cve.cvefor('cpe:/a:microsoft:office:2011::mac')


if __name__ == "__main__":
    unittest.main()
