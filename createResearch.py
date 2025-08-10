import json
import string

from mwcleric import AuthCredentials
from mwcleric import WikiggClient

WIKITEXT = """{{{{Research Infobox
|Name={Name}
|Requirement={Requirement}
|Cost={Cost}
|Time={Time}
|Category={Category}
}}}}"""


class Creator:
    def __init__(self):
        credentials = AuthCredentials(user_file="CargoBot")
        self.site = WikiggClient('witchfire', credentials=credentials)
        #self.summary = 'Tabber -> Gallery'
        with open('Research.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def run(self):
        PAGETEXT = ''
        for k, v in self.data.items():
            PAGETEXT = PAGETEXT + WIKITEXT.format(
                Name=k,             
                Requirement=v['Requirement'],
                Cost=v['Cost'],
                Time=v['Time'],
                Category=v['Category']
            )
        self.site.client.pages['Research Infobox'].save(PAGETEXT)

if __name__ == '__main__':
    Creator().run()