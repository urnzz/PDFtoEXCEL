import fitz
import os
dir_list = os.listdir(os.getcwd())
cpfs=[]
rs=[]
for file in dir_list:
     if '.pdf' in file:
          print(file)
          with fitz.open(file) as doc:
               for page in doc:
                    lines = page.get_text().replace('\n', '|').split(',')
                    n=0
                    for line in lines:
                         if 'CPF' in line:
                              cpfs.append(line.replace('\n','').strip().replace('CPF ',''))
                         elif 'RS/' in line:
                              rs.append(line.replace('\n','').strip())
with open('output.csv', 'w+', encoding="utf-8") as fo:
     print(len(rs))
     print(len(cpfs))
     t='RS/PV, CPF\n'
     n=0
     for line in rs:
          if len(line)<=10:
               t+=str(line.replace('RS/PV:','').replace('|','').strip()+','+cpfs[n].replace('|','')).replace('RS/PV:','').strip()+'\n'
               n+=1
          else:
               s=''
               nn=0
               for i in str(line.replace('RS/PV:','').replace('|','').strip()).replace('RS/PV:', '').strip():
                    if nn<=10:
                         s+=i
                         nn+=1
                    else:
                         nn+=1
               t+=str(s.replace('RS/PV:','').replace('|','').strip()+','+cpfs[n].replace('|','')).replace('RS/PV:','').strip()+'\n'
               n+=1
     fo.write(t)