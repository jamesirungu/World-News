class TopHeadlines:
    id = ''
    name = ''
    author = ''
    title = ''
    description = ''
    url = ''
    url_to_image = ''
    published_at = '',
    country = ''

    def __init__(self, id, name, author, title, description, url, url_to_image, published_at, country):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.url_to_image = url_to_image
        self.published_at = published_at
        self.country = country


class Sources:
    id = ''
    name = ''
    category = ''
    description = ''
    url = ''

    def __init__(self, id, name, description, url, category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
