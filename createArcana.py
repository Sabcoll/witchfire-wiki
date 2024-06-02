import json
import string

from mwcleric import AuthCredentials
from mwcleric import WikiggClient

WIKITEXT = """{{{{ArcanaInfobox
|Name={Name}
|Type={Type}
|Description={Description}
|Charismata={Charismata}
}}}}"""



class Creator:
    def __init__(self):
        credentials = AuthCredentials(user_file="me")
        self.site = WikiggClient('witchfire', credentials=credentials)
        #self.summary = 'Tabber -> Gallery'
        with open('arcana.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def run(self):
        PAGETEXT = ''
        for k, v in self.data.items():
            PAGETEXT = PAGETEXT + WIKITEXT.format(
                Name=k,              
                Type=v['Arcanum_Type'], 
                Description=v['Description'],
                Charismata=v['Charismata']
            )
        self.site.client.pages['ArcanaInfobox'].save(PAGETEXT)

if __name__ == '__main__':
    Creator().run()
    
