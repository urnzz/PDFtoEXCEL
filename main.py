import fitz
import os
dir_list = os.listdir(os.getcwd())
for file in dir_list:
     if '.pdf' in file:
          with open('output.csv', 'w+', encoding="utf-8") as fo:
               with fitz.open(file) as doc:
                    for page in doc:
                         lines = page.get_text().split('\n')
                              n=0
                              txt=''
                              for line in lines:
                                   if n == 0 or n == 1 or n == 2:
                                        n+=1
                                   else:
                                        txt+=(line+'\n')
                                        n+=1
                              sp=txt.split(',')      
                              fo.write('nome, cpf, rs/pv, cargo\n')
                              n=0
                              for i in sp:
                                   if n == 0:
                                        fo.write(i.strip()+', ')
                                        n+=1
                                   elif n == 1:
                                        fo.write(i.strip().replace('CPF ', '')+',')
                                   elif n == 2:
                                        fo.write(i.strip().replace('RS/PV: ', '')+',')
                                        n+=1
                                   elif n == 1:
                                        fo.write(i.strip()+'\n')
                                        n=0
                              
                              
