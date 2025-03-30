import json
import string

from mwcleric import AuthCredentials
from mwcleric import WikiggClient

WIKITEXT = """{{{{Prophecy Infobox
|Name={Name}
|Type={Type}
|Omen={Omen}
|Omen_Effect={Omen_Effect}
|Source={Source}
|UnlockedArcanum={UnlockedArcanum}
}}}}"""

class Creator:
    def __init__(self):
        credentials = AuthCredentials(user_file="me")
        self.site = WikiggClient('witchfire', credentials=credentials)
        #self.summary = 'Tabber -> Gallery'
        with open('Prophecies.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def run(self):
        PAGETEXT = ''
        for k, v in self.data.items():
            PAGETEXT = PAGETEXT + WIKITEXT.format(
                Name=k,          
                Type=v['Type'],
                Omen=v['Omen'],
                Omen_Effect=v['Omen_Effect'],
                Source=v['Source'],
                UnlockedArcanum=v['Unlocked_Arcanum'],
)
        self.site.client.pages['Prophecy Infobox'].save(PAGETEXT)

if __name__ == '__main__':
    Creator().run()
    
