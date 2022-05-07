class Config:
    NEWS_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={}'
    NEWS_API_KEY = 'f2888d530ffa4d9cb5ad1a5f9577bdff'
    NEWS_SOURCES_URL = 'https://newsapi.org/v2/top-headlines/sources?category={}&language={}&apiKey={}'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
