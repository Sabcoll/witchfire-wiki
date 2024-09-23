import json
import string

from mwcleric import AuthCredentials
from mwcleric import WikiggClient

class Creator:
    def __init__(self):
        credentials = AuthCredentials(user_file="me")
        self.site = WikiggClient('witchfire', credentials=credentials)
        #self.summary = 'Tabber -> Gallery'

    def run(self):
        for k in self.site.client.allpages(namespace=0):
            self.site.purge(k)
            print('Purging: ',k)


if __name__ == '__main__':
    Creator().run()
    
