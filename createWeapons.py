import json
import string

from mwcleric import AuthCredentials
from mwcleric import WikiggClient

WIKITEXT = """{{{{Weapon Infobox
|WRange={WRange}
|Type={Type}
|Starter={Starter}
|Source={Source}
|Element={Element}
|FireMode={FireMode}
|Damage={Damage}
|HeadshotMP={HeadshotMP}
|StunPower={StunPower}
|HipfireRange={HipfireRange}
|ADSRange={ADSRange}
|Stability={Stability}
|RateOfFire={RateOfFire}
|Mobility={Mobility}
|ClipSize={ClipSize}
|AmmoReserves={AmmoReserves}
|Lore={Lore}
|Description={Description}


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
                WRange=v['WRange'],
                Type=v['Type'],
                Starter=v['Starter'],
                Source=v['Source'],
                Element=v['Element'],
                FireMode=v['Fire_Mode'],
                Damage=v['Damage'],
                HeadshotMP=v['Headshot_Multiplier'],
                StunPower=v['Stun_Power'],
                HipfireRange=v['Hipfire_Range'],
                ADSRange=v['ADS_Range'],
                Stability=v['Stability'],
                RateOfFire=v['Rate_of_Fire'],
                Mobility=v['Mobility'],
                ClipSize=v['Clip_Size'],
                AmmoReserves=v['Ammo_Reserves'],
                Lore=v['Lore'],
                Description=v['Description']
            ))

if __name__ == '__main__':
    Creator().run()
