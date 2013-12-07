# bing.py by Adam Canady
# Dec 2013

import requests
import urllib
import json

class BingWebSearch(object):

	def __init__(self, key):
		self.key = key
		self.base_url = "https://api.datamarket.azure.com/Bing/SearchWeb/v1/Web?"

	def query(self, query, skip = 0):
		params = {
			"Query": "'"+query+"'",
			"$format": "JSON",
			"$skip": skip
		}

		url = self.base_url + urllib.urlencode(params)
		return self.fetch_url(url)

	def fetch_url(self, url):
		result = requests.get(url, auth=(self.key, self.key))
		parsed = json.loads(result.content)

		if parsed.get('d',''):
			self.next = parsed['d']['__next'] + "&$format=JSON" if parsed['d'].get('__next','') else ''
			if parsed['d'].get('results',''): return parsed['d']['results']

	def query_all(self, query, limit = float('inf')):
		results = self.query(query)
		count = 1
		while self.next and count < limit:
			results += self.fetch_url(self.next)
			count += 1

		return results
