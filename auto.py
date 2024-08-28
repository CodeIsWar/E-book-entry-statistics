import zipfile
import os
from bs4 import BeautifulSoup
import sys
import ahocorasick
f9=zipfile.ZipFile(sys.argv[1])
for file in f9.namelist():
    f9.extract(file,r'temp')
for findex in range(0,2):
    for index in range(0,10):
        try:
            xhtml_file=open(f"temp/OEBPS/Text/Section0{findex}{index}.xhtml",'r')
            xhtml_handle=xhtml_file.read()
            soup=BeautifulSoup(xhtml_handle,'lxml')
            p_list=soup.find_all('p')
            if(findex==0):
                with open(f'temp/out.{index}','w')as fil:
                    for p in p_list:
                        fil.write(p.text)
                        fil.write('\n')
            else:
                with open(f'temp/out.{findex}{index}','w')as fil:
                    for p in p_list:
                        fil.write(p.text)
                        fil.write('\n')
        except IOError:
            break
        except:
            print('error')
            exit()
aca=ahocorasick.Automaton()
citiao={}
with open(sys.argv[2],'r')as f2:
    keywords=[a.strip() for a in f2.readlines()]
for x in range(len(keywords)):
    aca.add_word(keywords[x],(x,keywords[x]))
    citiao[keywords[x]]=0
aca.make_automaton()
for i in range(0,20):
    try:
        with open(f'temp/out.{i}','r')as f1:
            fitext=f1.read()
        for item in aca.iter(fitext):
            citiao[item[1][1]]+=1
    except:
        break
for kword in keywords:
    print(kword,end='')
    print(citiao[kword])
