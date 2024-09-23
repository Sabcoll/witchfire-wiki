import json
import string

from mwcleric import AuthCredentials
from mwcleric import WikiggClient

WIKITEXT = """{{{{Weapon Infobox
|Research={Research}
|Type={Type}
|FireMode={FireMode}
|Damage={Damage}
|StunPower={StunPower}
|HipfireRange={HipfireRange}
|ADSRange={ADSRange}
|Stability={Stability}
|RateOfFire={RateOfFire}
|Mobility={Mobility}
|ClipSize={ClipSize}
|Lore={Lore}
|Description={Description}
|HeadshotMP={HeadshotMP}
|Element={Element}
}}}}"""


class Creator:
    def __init__(self):
        credentials = AuthCredentials(user_file="me")
        self.site = WikiggClient('witchfire', credentials=credentials)
        #self.summary = 'Tabber -> Gallery'
        with open('weapons.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def run(self):
        for k, v in self.data.items():
            self.site.client.pages[string.capwords(k)].save(WIKITEXT.format(
                Research=v['Research'],
                Type=v['Type'],              
                FireMode=v['Fire_Mode'], 
                Damage=v['Damage'], 
                StunPower=v['Stun_Power'], 
                HipfireRange=v['Hipfire_Range'], 
                ADSRange=v['ADS_Range'], 
                Stability=v['Stability'], 
                RateOfFire=v['Rate_of_Fire'], 
                Mobility=v['Mobility'], 
                ClipSize=v['Clip_Size'], 
                Lore=v['Lore'], 
                Description=v['Description'],
                HeadshotMP=v['Headshot_Multiplier'],
                Element=v['Element']
            ))

if __name__ == '__main__':
    Creator().run()
