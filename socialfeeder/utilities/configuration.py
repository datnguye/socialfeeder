import bs4
from lxml import etree
import os
from socialfeeder.utilities.common import ObjectView, save_to_json_file

def parse(path:str, save:bool=False):
    '''
    Parse xml document to dict object
    '''
    # Load xml
    print(f'INFO: XML file at: {path}')
    lxml_content = open(file=path,mode="r",encoding="utf8").read()
    soup = bs4.BeautifulSoup(lxml_content, "lxml")
    
    # Load xml schema - xsd to validate
    xsd_path = f'{os.path.dirname(os.path.realpath(__file__))}/configuration.xsd'
    # valid, message = validate(xml_path=path, xsd_path=xsd_path)
    # if not valid:
    #     print(f'ERROR: Failed at validation with message: {message}')
    #     return None
    
    results = []
    pages = soup.findAll("page")
    for page in pages:
        # result - base
        result = {
            "config_at": os.path.abspath(path),
            "targets": {
                "limit_post": page.find("targets").get("limit-post"),
                "method": page.find("targets").get("method").split(':')[0],
                "attr": page.find("targets").get("method").split(':')[1],
                "method_val": page.find("targets").get("method-val")
            },
            "actions": parse_actions(page.find("actions"))
        }

        results.append(ObjectView(result))
        
    if save:
        save_to_json_file(results[0].origin, path.replace('.xml', '.json'))
    return results


def parse_actions(soup):
    '''
    Function to parse "action" nodes
    '''
    actions = []
    for a in soup.find_all("action", recursive=False):
        actions.append({
            "name": a.get("name") or "not-set",
            "url": a.get("url") or '',
            "type": a.get("type"),
            "value": a.get("value") or '',
            "xpath_to": a.get("xpath-to") or ''
        })
    
    return actions

def validate(xml_path:str, xsd_path:str) -> bool:
    '''
    Validate xml schema of the config file
    '''
    # xmlschema_doc = etree.parse(xsd_path)
    # xmlschema = etree.XMLSchema(xmlschema_doc)

    # xml_doc = etree.parse(xml_path)
    # result = xmlschema.validate(xml_doc)

    pass #return (result, xmlschema.error_log)