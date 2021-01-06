# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 23:00:18 2020

@author: Denis

Downloads all practice problem answers, in all 35 Chapters,
for Algorithms textbook. Downloads into directory where you ran the script
"""

import urllib.request


suffix = ".pdf"
link_first_part = "https://sites.math.rutgers.edu/~ajl213/CLRS/Ch"


for i in range(1, 36):
    whole_link = link_first_part + str(i) + suffix
    response = urllib.request.urlopen(whole_link)
    file = open("Chapter " + str(i) + ".pdf", 'wb')
    file.write(response.read())
    file.close()
    

