import json,os


def printf(text):
    try:
     print('\033[1;35m'+text+'\033[0m')
     print(" ")
    except Exception as f:
         print(f)
def file_write(filename,data1,data2,data3,data4,data5,data6,data7,data8,data9):
    try:
         j = json.load(open(filename))

    except:
         o = {}
         o['test']= 'test'
         with open(filename,'+a') as f:
           json.dump(o,f,indent=4)
         os.system('touch '+filename)
         j = json.load(open(filename))
    try:
     del j['test']
    except:
         pass
    j[data1] = [data2]
    j[data1].append(data3)
    j[data1].append(data4)
    j[data1].append(data5)
    j[data1].append(data6)
    j[data1].append(data7)
    j[data1].append(data8)
    j[data1].append(data9)
    with open(filename,'w') as f:
         json.dump(j,f,indent=5)



def data_view(filename):
     try:
          data = json.load(open(filename))
     except:
          printf("data not found ")
     co = 0
     for i in data:
          print("")
          printf(i)
          for b in data[i]:
               printf("")
               printf("")
               printf("\033[1;33m"+b)

          printf("------------------"*4)






￼Enter
