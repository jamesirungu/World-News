class Config:
    NEWS_API_BASE_URL='https://newsapi.org/v2/top-headlines?country={}&apiKey={}'
    NEWS_API_KEY = '3a33361e0e2d42cda7b68efdbdeb1ff6'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}