import json
import string

from mwcleric import AuthCredentials
from mwcleric import WikiggClient

WIKITEXT = """{{{{AlchemyInfobox
|Name={Name}
|Effect={Effect}
|Ing1Amount={Ing1Amount}
|Ingredient1={Ingredient1}
|Ing2Amount={Ing2Amount}
|Ingredient2={Ingredient2}
|Location={Location}
|Source={Source}
|Note={Note}
}}}}"""


class Creator:
    def __init__(self):
        credentials = AuthCredentials(user_file="me")
        self.site = WikiggClient('witchfire', credentials=credentials)
        #self.summary = 'Tabber -> Gallery'
        with open('Incenses.json', 'r', encoding='utf8') as f:
            self.data = json.load(f)

    def run(self):
        for k, v in self.data.items():
            self.site.client.pages[string.capwords(k)].save(WIKITEXT.format(
                Name=k,
                Effect=v['Effect'],
                Ing1Amount=v['Ing1_Amount'],
                Ingredient1=v['Ingredient_1'],
                Ing2Amount=v['Ing2_Amount'],
                Ingredient2=v['Ingredient_2'],
                Location=v['Location'],
                Source=v['Source'],
                Note=v['Note']
            ))

if __name__ == '__main__':
    Creator().run()
