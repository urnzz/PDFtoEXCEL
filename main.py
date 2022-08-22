import fitz
import os
dir_list = os.listdir(os.getcwd())
l='nome, cpf, rs/pv, cargo\n'
for file in dir_list:
     if '.pdf' in file:
          print(file)
          with fitz.open(file) as doc:
               for page in doc:
                    lines = page.get_text().split('\n')
                    n=0
                    txt=''
                    for line in lines:
                         if 'CPF' not in line or 'RS/' not in line or '-' not in line:
                              n+=1
                         else:
                              txt+=(line+'\n')
                              n+=1
                    sp=txt.split(',')      
                    n=0
                    for i in sp:
                         if n == 0:
                              l+=(i.strip()+', ')
                              n+=1
                         elif n == 1:
                              l+=(i.strip().replace('CPF ', '')+',')
                         elif n == 2:
                              l+=(i.strip().replace('RS/PV: ', '')+',')
                              n+=1
                         elif n == 1:
                              l+=(i.strip()+'\n')
                              n=0
with open('output.csv', 'w+', encoding="utf-8") as fo:
     fo.write(l)
                              
