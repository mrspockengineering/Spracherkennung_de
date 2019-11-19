'''
Created on 17.11.2019

@author: Erazer
'''

import webbrowser
import re

def oeffne_seite(arg="heise.de"):
    command = "öffne seite"+ arg
    if 'öffne seite' in command:
        reg_ex = re.search('öffne seite(.*)', command)
        # print reg_ex
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Fertig')
            
            
oeffne_seite("tagesschau.de")
webbrowser.open("https://www.youtube.de")