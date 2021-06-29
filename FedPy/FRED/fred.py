"""
    Modified version of FRED api 
    Credits to: Mortada, for original version (https://github.com/mortada/fredapi) 
"""
import os
import sys
import xml.etree.ElementTree as ET
if sys.version_info[0] >= 3:
    import urllib.request as url_request
    import urllib.parse as url_parse
    import urllib.error as url_error
else:
    import urllib2 as url_request
    import urllib as url_parse
    import urllib2 as url_error

import pandas as pd

urlopen = url_request.urlopen
quote_plus = url_parse.quote_plus
urlencode = url_parse.urlencode
HTTPError = url_error.HTTPError


class Fred(object):
    earliest_realtime_start = '1776-07-04'
    latest_realtime_end = '9999-12-31'
    nan_char = '.'
    max_results_per_request = 1000
    root_url = 'https://api.stlouisfed.org/fred'

    def __init__(self,
                 api_key=None,
                 api_key_file=None):
        """
        Initialize the Fred class that provides useful functions to query the Fred dataset. You need to specify a valid
        API key in one of 3 ways: pass the string via api_key, or set api_key_file to a file with the api key in the
        first line, or set the environment variable 'FRED_API_KEY' to the value of your api key. You can sign up for a
        free api key on the Fred website at http://research.stlouisfed.org/fred2/
        """
        self.api_key = None
        if api_key is not None:
            self.api_key = api_key
        elif api_key_file is not None:
            f = open(api_key_file, 'r')
            self.api_key = f.readline().strip()
            f.close()
        else:
            self.api_key = os.environ.get('FRED_API_KEY')

        if self.api_key is None:
            import textwrap
            raise ValueError(textwrap.dedent("""\
                    You need to set a valid API key. You can set it in 3 ways:
                    pass the string with api_key, or set api_key_file to a
                    file with the api key in the first line, or set the
                    environment variable 'FRED_API_KEY' to the value of your
                    api key. You can sign up for a free api key on the Fred
                    website at http://research.stlouisfed.org/fred2/"""))

    def __fetch_data(self, url):
        """
        helper function for fetching data given a request URL
        """
        url += '&api_key=' + self.api_key
        try:
            response = urlopen(url)
            root = ET.fromstring(response.read())
        except HTTPError as exc:
            root = ET.fromstring(exc.read())
            raise ValueError(root.get('message'))
        return root

    def _parse(self, date_str, format='%Y-%m-%d'):
        """
        helper function for parsing FRED date string into datetime
        """
        rv = pd.to_datetime(date_str, format=format)
        if hasattr(rv, 'to_pydatetime'):
            rv = rv.to_pydatetime()
        return rv

    def get_series(self, series_id, start=None, end=None):
        url = "%s/series/observations?series_id=%s" % (self.root_url, series_id)
        
        if start is not None:
            start = pd.to_datetime(start,
                                               errors='raise')
            url += '&observation_start=' + start.strftime('%Y-%m-%d')
        
        if end is not None:
            end = pd.to_datetime(end, errors='raise')
            url += '&observation_end=' + end.strftime('%Y-%m-%d')
        
        root = self.__fetch_data(url)
        
        if root is None:
            raise ValueError('No data exists for series id: ' + series_id)
        
        data = {}

        for child in root:
            val = child.get('value')
            if val == self.nan_char:
                val = float('NaN')
            else:
                val = float(val)
            data[self._parse(child.get('date'))] = val

        return pd.Series(data)
