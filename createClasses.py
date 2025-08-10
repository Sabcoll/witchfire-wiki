import json
import string

from mwcleric import AuthCredentials
from mwcleric import WikiggClient

WIKITEXT = """{{{{Class Infobox
|Starting_Level={StartingLevel}
|Flesh={Flesh}
|Blood={Blood}
|Mind={Mind}
|Witchery={Witchery}
|Arsenal={Arsenal}
|Faith={Faith}
|Weapon1={Weapon1}
|Weapon2={Weapon2}
|Spell1={Spell1}
|Spell2={Spell2}
|Gear1={Gear1}
|Gear2={Gear2}
|Description={Description}
}}}}"""


class Creator:
    def __init__(self):
        credentials = AuthCredentials(user_file="CargoBot")
        self.site = WikiggClient('witchfire', credentials=credentials)
        #self.summary = 'Tabber -> Gallery'
        with open('Classes.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def run(self):
        for k, v in self.data.items():
            self.site.client.pages[string.capwords(k)].save(WIKITEXT.format(
                StartingLevel=v['Starting_Level'],
                Flesh=v['Flesh'],
                Blood=v['Blood'],
                Mind=v['Mind'],
                Witchery=v['Witchery'],
                Arsenal=v['Arsenal'],
                Faith=v['Faith'],
                Weapon1=v['Weapon1'],
                Weapon2=v['Weapon2'],
                Spell1=v['Spell1'],
                Spell2=v['Spell2'],
                Gear1=v['Gear1'],
                Gear2=v['Gear2'],
                Description=v['Description']
            ))

if __name__ == '__main__':
    Creator().run()
