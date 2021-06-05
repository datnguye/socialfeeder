from socialfeeder.engines import facebook
from socialfeeder.utilities import configuration
from socialfeeder.utilities.constants import *

def run(social:str=None, config:dict=None):
    '''
    Run feeding
    '''
    config_obj = configuration.parse(config, save=True)

    result = {}
    if social == FEEDER_FACEBOOK:
        result = facebook.run(config=config_obj)
    else:
        print(f'Other social is not supported yet!')
    
    print(result)