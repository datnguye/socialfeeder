from socialfeeder.engines import facebook
from socialfeeder.utilities import configuration

def run(social:str=None, config:dict=None):
    '''
    run
    '''
    config_obj = configuration.parse(config, save=True)
    if social == 'facebook':
        facebook.run(config_obj)
    else:
        print(f'Other social is not supported yet!')
