import json
import string

from mwcleric import AuthCredentials
from mwcleric import WikiggClient

WIKITEXT = """{{{{Bead Infobox
|Name={Name}
|Effect={Effect}
|Requirement={Requirement}
|Map={Map}
|Location={Location}
}}}}"""

class Creator:
    def __init__(self):
        credentials = AuthCredentials(user_file="CargoBot")
        self.site = WikiggClient('witchfire', credentials=credentials)
        #self.summary = 'Tabber -> Gallery'
        with open('Beads.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def run(self):
        PAGETEXT = ''
        for k, v in self.data.items():
            PAGETEXT = PAGETEXT + WIKITEXT.format(
                Name=k,          
                Effect=v['Effect'],
                Requirement=v['Requirement'],
                Map=v['Map'],
                Location=v['Location'],
)
        self.site.client.pages['Bead Infobox'].save(PAGETEXT)

if __name__ == '__main__':
    Creator().run()
    
