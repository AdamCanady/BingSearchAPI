import bing
import pprint

b = bing.BingWebSearch("api_key_here")
results = b.query_all("apples", limit = 3) # limit not required

pprint.pprint(results)

results = b.query("apples")

pprint.pprint(results)
