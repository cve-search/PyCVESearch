[![Python application](https://github.com/cve-search/PyCVESearch/actions/workflows/mypy.yml/badge.svg)](https://github.com/cve-search/PyCVESearch/actions/workflows/mypy.yml)

**PyCVESearch** is an easy to use wrapper around cve-search. Some of the calls will work against https://cve.circl.lu but for most of them, you need your own CVE Search instance.

This library is based on the work of [Martin Simon](https://github.com/mrsmn/ares) and [Kai Renken](https://github.com/elektrischermoench/ares3).

**Important Note**: The API endpoint has been removed from the public instance due to massive abusive behavior. You can use this API against a local version of CVE Search.


## Installation:

From source use

```
    $ pip install pycvesearch
```

## Documentation:

- **`GET /api/browse/`**
- **`GET /api/browse/vendor`**

```python
>>> from pycvesearch import CVESearch
>>> cve = CVESearch()
>>> cve.browse(<vendor>)
```

- **`GET /api/search/vendor/product`**

```python
>>> cve.search('microsoft/office')
```

- **`GET /api/cveid/cveid`**

```python
>>> cve.id('CVE-2014-0160')
```

- **`GET /api/last`**

```python
>>> cve.last()
```

- **`GET /api/dbInfo`**

```python
>>> cve.dbinfo()
```

- **`GET /api/cpe2.2/cpe`**

```python
>>> cve.cpe22('cpe:/a:microsoft:office:2011::mac')
```

- **`GET /api/cpe2.3/cpe`**

```python
>>> cve.cpe23('cpe:2.3:a:microsoft:office:2011:-:mac')
```

- **`GET /api/cvefor/cpe`**

```python
>>> cve.cvefor('cpe:/a:microsoft:office:2011::mac')
```

## License:

```
    Apache v2.0 License
    Copyright 2015-2016 Martin Simon
    Copyright 2015-2016 Kai Renken
    Copyright 2016 Raphaël Vinot

     Licensed under the Apache License, Version 2.0 (the "License");
     you may not use this file except in compliance with the License.
     You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

     Unless required by applicable law or agreed to in writing, software
     distributed under the License is distributed on an "AS IS" BASIS,
     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     See the License for the specific language governing permissions and
     limitations under the License.

```
