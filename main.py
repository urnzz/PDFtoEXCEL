import fitz
import fitz
import os
import csv
dir_list = os.listdir(os.getcwd())
l=['nome', 'cpf', 'rs/pv', 'cargo']
txt=''
for file in dir_list:
     if '.pdf' in file:
          print(file)
          with fitz.open(file) as doc:
               for page in doc:
                    lines = page.get_text().replace('\n', '|')
                    n=0
                    for i in lines.split('|'):
                         if n<=2:
                              n+=1
                         elif n % 2 == 0:
                              txt+=i
                              n+=1
                         else:
                              txt+=i+'\n'
                              n+=1
with open('output.csv', 'w+', encoding="utf-8") as fo:
     w = csv.writer(fo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
     w.writerow(l)
     fo.write(str(txt))
