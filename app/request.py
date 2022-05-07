import urllib.request, json
from .models import TopHeadlines, Sources

api_key = None
sources_url = None
headlines_url = None


def configure_request(app):
    global api_key, sources_url, headlines_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['NEWS_SOURCES_URL']
    headlines_url = app.config['NEWS_HEADLINES_URL']


def getHeadlines(country):
    my_url = headlines_url.format(country, api_key)
    with urllib.request.urlopen(my_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)
        headlines_results = None
        if get_headlines_response['articles']:
            headlines_results_list = get_headlines_response['articles']
            headlines_results = processHeadLinesResult(headlines_results_list, country)
    return headlines_results


def processHeadLinesResult(headlines_results_list, country):
    results = []
    for item in headlines_results_list:
        id = item.get('id')
        name = item.get('name')
        author = item.get('author')
        url = item.get('url')
        title = item.get('title')
        url_to_image = item.get('urlToImage')
        published_at = item.get('publishedAt')
        description = item.get('description')
        country = country
        if url:
            headlines = TopHeadlines(id, name, author, title, description, url, url_to_image, published_at, country)
            results.append(headlines)
    return results


def getSources(category, language):
    my_url = sources_url.format(category, language)
    with urllib.request.urlopen(my_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.load(get_sources_data)
        sources_results = None
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = processSourcesResult(sources_results_list)
    return sources_results


def processSourcesResult(sources_results_list):
    results = []
    for item in sources_results_list:
        id = item.get('id')
        name = item.get('name')
        url = item.get('url')
        description = item.get('description')
        category = item.get('category')
        if url:
            sources = Sources(id, name, category, description, url)
            results.append(sources)
    return results
