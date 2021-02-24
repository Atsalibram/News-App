class Config:
    '''
    General configuration parent class
    '''
    pass
    NEWS_API_BASE_URL ='https://newsapi.org/account/{}?api_key=1a6a17f1f4484376ad766f22c4896f3b'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}
