import json
import string

from mwcleric import AuthCredentials
from mwcleric import WikiggClient

WIKITEXT = """{{{{MagicalItem Infobox
|Type={Type}
|Element={Element}
|Starter={Starter}
|Source={Source}
|Power={Power}
|Lore={Lore}
}}}}"""


class Creator:
    def __init__(self):
        credentials = AuthCredentials(user_file="me")
        self.site = WikiggClient('witchfire', credentials=credentials)
        #self.summary = 'Tabber -> Gallery'
        with open('MagicalItems.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def run(self):
        for k, v in self.data.items():
            self.site.client.pages[string.capwords(k)].save(WIKITEXT.format(
                Type=v['Type'],              
                Lore=v['Lore'], 
                Power=v['Power'],
                Source=v['Source'], 
                Element=v['Element'],
                Starter=v['Starter']
            ))

if __name__ == '__main__':
    Creator().run()
