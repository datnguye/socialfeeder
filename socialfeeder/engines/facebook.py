from socialfeeder.engines import core as chrome
from socialfeeder.utilities.constants import *
from socialfeeder.utilities import configuration
from datetime import datetime, timedelta

def run(config, debug:bool=True):
    
    result = {
        'start_at': datetime.now(),
        'res_stack': []
    }
    
    if debug: print(f'[feeder] Starting feeding...')
    if debug: print(f'[feeder]  Open new driver instance.')
    driver = chrome.get_instance(headless=False)

    if debug: print(f'[feeder]  Running actions...')
    for action_group in config:
        for action in action_group.actions:
            if action.type == ACTION_TYPE_WAIT:
                code, res = _do_wait(driver, action, debug=debug, indent=2)
            elif action.type == ACTION_TYPE_BROWSE:
                code, res = _do_browse(driver, action, debug=debug, indent=2)
            elif action.type == ACTION_TYPE_CLICK:
                code, res = _do_click(driver, action, debug=debug, indent=2)
            elif action.type == ACTION_TYPE_FILL:
               code, res =  _do_fill(driver, action, debug=debug, indent=2)
            else:
                code, res = -1, 'Non-support action'
                if debug: print(f'[feeder]      Non-support action! Please contact ADMIN.')
            
            result['res_stack'].append({ 'action': action.name, 'code':code, 'message': res})

    result['end_at'] = datetime.now()
    result['duration_in_s'] = (result['end_at'] - result['start_at']).total_seconds()
    if debug: print(f'[feeder] Finished.')

    return result

def _do_wait(driver, action, debug:bool=False, indent:int=1):
    if debug: print(f'[feeder] {" "*indent}Doing {action.name}')
    try:
        chrome.browse(driver)
    except Exception as e:
        if not action.bypass_error:
            return (-1, f'{action.name} failed with message: {str(e)}')
    
    return (0, f'{action.name} succeeded')


def _do_browse(driver, action, debug:bool=False, indent:int=1):
    if debug: print(f'[feeder] {" "*indent}Doing {action.name}')
    try:
        chrome.scroll_down_bottom(driver)
    except Exception as e:
        if not action.bypass_error:
            return (-1, f'{action.name} failed with message: {str(e)}')

    return (0, f'{action.name} succeeded')


def _do_click(driver, action, debug:bool=False, indent:int=1):
    if debug: print(f'[feeder] {" "*indent}Doing {action.name}')
    try:
        elements = driver.find_elements_by_xpath(action.xpath_to)

        limit = len(elements)
        if limit > int(action.value):
            limit = int(action.value)
        elements = elements[0:limit]
        for e in elements:
            e.click()
    except Exception as e:
        if not action.bypass_error:
            return (-1, f'{action.name} failed with message: {str(e)}')

    return (0, f'{action.name} succeeded')

    
def _do_fill(driver, action, debug:bool=False, indent:int=1):
    if debug: print(f'[feeder] {" "*indent}Doing {action.name}')
    try:
        elements = driver.find_elements_by_xpath(action.xpath_to)
        for e in elements:
            e.send_keys(action.value)
    except Exception as e:
        if not action.bypass_error:
            return (-1, f'{action.name} failed with message: {str(e)}')
    return (0, f'{action.name} succeeded')

