import json
import string

from mwcleric import AuthCredentials
from mwcleric import WikiggClient

WIKITEXT = """{{{{Item infobox
|Name={Name}
|Research={Research}
|Type={Type}
|Fire_Mode={Fire_Mode}
|Damage={Damage}
|Stun_Power={Stun_Power}
|Hipfire_Range={Hipfire_Range}
|ADS_Range={ADS_Range}
|Stability={Stability}
|Rate_of_Fire={Rate_of_Fire}
|Mobility={Mobility}
|Clip_Size={Clip_Size}
|Lore={Lore}
|Description={Description}
}}}}"""


class Creator:
    def __init__(self):
        credentials = AuthCredentials(user_file="me")
        self.site = WikiggClient('witchfire.wiki.gg', credentials=credentials)
        self.summary = 'Tabber -> Gallery'
        with open('weapons.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def run(self):
        for k, v in self.data.items():
            self.site.client.pages[string.capwords(k)].save(WIKITEXT.format(
                Name =v['Research'],
                Research=v['Research'],
                Type=v['Type'],              
                Fire_Mode=v['Fire_Mod'], 
                Damage=v['Damage'], 
                Stun_Power=v['Stun_Power'], 
                Hipfire_Range=v['Hipfire_Range'], 
                ADS_Range=v['ADS_Range'], 
                Stability=v['tability'], 
                Rate_of_Fire=v['Rate_of_Fire'], 
                Mobility=v['Mobility'], 
                Clip_Size=v['Clip_Size'], 
                Lore=v['Lore'], 
                Description=v['Description'] 
            ))

if __name__ == '__main__':
    Creator().run()
