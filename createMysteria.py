import json
import string

from mwcleric import AuthCredentials
from mwcleric import WikiggClient

WIKITEXT = """{{{{Mysteria Infobox
|RowNo={RowNo}
|Name={Name}
|Mysterium={Mysterium}
|Requirement1={Requirement1}
|Requirement2={Requirement2}
|Requirement3={Requirement3}
|Description={Description}
|Charismata1={Charismata1}
|Charismata2={Charismata2}
|Charismata3={Charismata3}
|Charismata4={Charismata4}
|Charismata5={Charismata5}
}}}}"""


class Creator:
    def __init__(self):
        credentials = AuthCredentials(user_file="me")
        self.site = WikiggClient('witchfire', credentials=credentials)
        #self.summary = 'Tabber -> Gallery'
        with open('mysteria.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def run(self):
        PAGETEXT = ''
        for k, v in self.data.items():
            PAGETEXT = PAGETEXT + WIKITEXT.format(
                RowNo=k,
                Name=v['Name'],             
                Mysterium=v['Mysterium'],
                Requirement1=v['Requirement_1'],
                Requirement2=v['Requirement_2'],
                Requirement3=v['Requirement_3'],
                Description=v['Description'],
                Charismata1=v['Charismata_1'],
                Charismata2=v['Charismata_2'],
                Charismata3=v['Charismata_3'],
                Charismata4=v['Charismata_4'],
                Charismata5=v['Charismata_5'],
            )
        self.site.client.pages['Mysteria Infobox'].save(PAGETEXT)

if __name__ == '__main__':
    Creator().run()
    
