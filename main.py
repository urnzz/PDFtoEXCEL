import os
import csv
from bs4 import BeautifulSoup
import aspose.words as aw
dir_list = os.listdir(os.getcwd())
l=['nome', 'cpf', 'rs/pv', 'cargo']
cpfs=[]
nomes=[]
rs=[]
cargo=[]
for file in dir_list:
     if '.pdf' in file:
          print(file)
          doc = aw.Document(file)
          doc.save("tmp.html")
          with open("tmp.html", "r") as doc:
                    soup = BeautifulSoup(doc, 'html.parser')
                    lines = soup.prettify().replace('\n', '|').split(',')
                    n=0
                    for item in lines:
                         ui = item.replace('\n', '').replace('RS/PV: ', '').replace('RS/', '').replace('CPF ','').replace('PV: ', '').strip()
                         if n==0 or n==1:
                              n+=1
                         elif n==2:
                              s=ui.split('|')
                              nomes.append(s[1])
                              n+=1
                         elif ui[0] == '|':
                              if ui != '' and len(ui.split(' ')) == 1:
                                   rs.append(ui.replace('|', ''))
                                   n+=1
                         elif '-|' in ui:
                              if ui != '':
                                   rs.append(ui.replace('|', ''))
                                   n+=1
                         elif '|' in item:
                              b = ui.split('|')
                              if len(b)==2:
                                   nomes.append(b[1])
                                   cargo.append(b[0])
                              elif len(b)==3:
                                   nomes.append(b[2])
                                   cargo.append(b[0]+b[1])
                              n+=1
                         elif 'CPF' in item :
                              if ui != '':
                                   cpfs.append(ui)
                                   n+=1
                    print(len(rs))
                    print(len(cpfs))
                    print(len(nomes))
                    print(len(cargo))
          with open('output.csv', 'w+', encoding="utf-8") as fo:
               w = csv.writer(fo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
               w.writerow(l)
               n=0
               if len(rs) == len(cpfs) == len(nomes):
                    for i in cpfs:
                         w.writerow([nomes[n],cpfs[n],rs[n],cargo[n]])
                         n+=1
               else:
                    print('error, file not saved')
