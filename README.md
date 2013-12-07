BingSearchAPI
=============

## Usage

To use this module, you'll need the `requests` library. It has been tested with Python 2.7.3. You'll also need a Bing Search API:

* Get your API key from http://www.bing.com/developers/
* For the Bing Search API schema, go to http://www.bing.com/developers/

Once you have your key and `requests` installed (`pip install requests`):

#### Simple

    import bing

    b = bing.BingWebSearch("api_key_here")
    results = b.query("apples")

#### All

    import bing

    b = bing.BingWebSearch("api_key_here")
    results = b.query_all("apples", limit = 3) # limit not required

See [`examples.py`](https://github.com/AdamCanady/BingSearchAPI/blob/master/examples.py) for more.

Released under MIT License by Adam Canady, December 6, 2013.
