from pprint import pprint

mailers = {}
file = open('myOutput.txt','r',encoding="utf-8")

while True:
    data = file.readline()
    if data is '': break
    
    print('-',data)
    s = data
    s = s[s.find("<")+1:s.find(">")]
    data = s

    try:
        mailers[data]+=1
    except:
        mailers[data]=1

op_file = open('counted.csv','w')

for key in mailers.keys():
    text = f"{key},{mailers[key]}\n"
    op_file.write(text) 

op_file.close()

pprint(mailers)