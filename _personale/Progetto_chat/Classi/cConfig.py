import json
import os


class Config:
    
    def __init__(self, cfgFile):
           
        self.ConfigFile = cfgFile
        print(os.path.abspath(self.ConfigFile))
        self.DBFile = ''

    def LeggiConfig(self):

        with open(self.ConfigFile, 'r', encoding = 'utf-8') as fr:
            datiGrezzi = fr.read()

        dicJson = json.loads(datiGrezzi)

        self.DBFile = dicJson['DBFILE']

