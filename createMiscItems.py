import json
import string

from mwcleric import AuthCredentials
from mwcleric import WikiggClient

WIKITEXT = """{{{{MiscItem Infobox
|Type={Type}
|Description={Description}
|Lore={Lore}
|Stash={Stash}
|Purchasable={Purchasable}
|Price={Price}
|Worth={Worth}
}}}}"""


class Creator:
    def __init__(self):
        credentials = AuthCredentials(user_file="me")
        self.site = WikiggClient('witchfire', credentials=credentials)
        #self.summary = 'Tabber -> Gallery'
        with open('MiscItem.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def run(self):
        PAGETEXT = ''
        for k, v in self.data.items():
            self.site.client.pages[string.capwords(k)].save(WIKITEXT.format(           
                Type=v['Type'],
                Description=v['Description'],
                Lore=v['Lore'],
                Stash=v['Stash'],
                Purchasable=v['Purchasable'],
                Price=v['Price'],
                Worth=v['Worth']
            ))
        self.site.client.pages['MiscItem Infobox'].save(PAGETEXT)

if __name__ == '__main__':
    Creator().run()