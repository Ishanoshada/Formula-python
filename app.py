import requests,bs4,json,os,file
#from data import  file
def inputf(text):
    try:
     data = input('\033[1;32m'+text+'\033[0m')
     return data
    except Exception as f:
         print(f)
         

def data_prin(filename):
     try:
        jdata = json.load(open(filename))
        return  jdata
     except json.decoder.JSONDecodeError as h:
         print(f'error for file data view :  {str(h)} ')
         
def printf(text):
    try:
     print('\033[1;33m'+text+'\033[0m')
     print(" ")
    except Exception as f:
         print(f)
def printft(text,text2):
    try:
     print('\033[1;36m ')
     print(text+'\033[0m  : \033[1;34m '+text2)
     print('\033[0m')
    except Exception as f:
         printf(f)
     
   
    



def get_formula_det(url):
   try:
    req = requests.get(url,headers=head)
    soup = bs4.BeautifulSoup(req.content.decode('utf-8'),'html.parser')
    data = soup.find_all('li')
    
    
    if data in []:
         printf('data not found ')
    else:
     data1 = soup.find_all('img',{'class':'struct'})
     #print(soup)
     Formulai = soup.find_all('h1',{'id':'Top'})
     Formula = data[14].text
     Molecular_weight  = data[15].text
     IUPAC_Standard_InChI = data[16].text
     IUPAC_Standard_InChIKey = data[17].text
     CAS_Registry_Number = data[18].text
     Chemical_structure =  'Chemical_structure link click to view  : '+ 'https://webbook.nist.gov/'+ data1[0]['src']
     Isotopologues =data[20].text
     Other_names = data[21].text
     printf('Formula name : '+Formulai[0].text)
     printf(Formula)
     printf(Molecular_weight)
#     printf(IUPAC_Standard_InChI)
 #    printf(IUPAC_Standard_InChIKey)
#     printf(CAS_Registry_Number)
     printf(Chemical_structure)
     
#     printf(Isotopologues)
     printf(Other_names)
     printf('MORE INFORMATION : '+url)
     cho= inputf('----> ENTER FOR DOWNLOAD DATA (d/e) ')
     if 'd' in cho:
          file.file_write('data/data_.txt',Formulai[0].text,Formula,Molecular_weight,IUPAC_Standard_InChI,IUPAC_Standard_InChIKey,CAS_Registry_Number,Chemical_structure,Isotopologues,Other_names)
          
          
     else:
          pass
   except Exception as f:
         printf(f)
     
     
     
     
     
     



#https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Units=SI



head = {
"Host": "webbook.nist.gov",
"Connection": "keep-alive",
"Cache-Control": "max-age=0",
"DNT": "1",
"Save-Data": "on",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/999.999.99 (Linux; Android 10; USER) AppleWebKit/999999.9 (KHTML, like Gecko) Chrome/999.9...9.. Mobile Safari/99.99.999",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

"Sec-Fetch-Site": "none",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-User":"?1",
"Sec-Fetch-Dest": "document",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "si,en;q=0.9,en-US;q=0.8,en-GB;q=0.7",

}

def get_formula(url):
 try:
   req = requests.get(url)
   

   soup = bs4.BeautifulSoup(req.content.decode('utf-8'),'html.parser')

   a = soup.find_all("a")
  # print(req.url)
   img = soup.find_all('img')
   a_for = []
   
   for i in a:
     if '/cgi/cbook.cgi?ID=' in i['href']:
         a_for.append(i)
     else:
          pass

   co = 0
   try:
    for i in a_for:
import requests,bs4,json,os,file
#from data import  file
def inputf(text):
    try:
     data = input('\033[1;32m'+text+'\033[0m')
     return data
    except Exception as f:
         print(f)
         

def data_prin(filename):
     try:
        jdata = json.load(open(filename))
        return  jdata
     except json.decoder.JSONDecodeError as h:
         print(f'error for file data view :  {str(h)} ')
         
def printf(text):
    try:
     print('\033[1;33m'+text+'\033[0m')
     print(" ")
    except Exception as f:
         print(f)
def printft(text,text2):
    try:
     print('\033[1;36m ')
     print(text+'\033[0m  : \033[1;34m '+text2)
     print('\033[0m')
    except Exception as f:
         printf(f)
     
   
    



def get_formula_det(url):
   try:
    req = requests.get(url,headers=head)
    soup = bs4.BeautifulSoup(req.content.decode('utf-8'),'html.parser')
    data = soup.find_all('li')
    
    
    if data in []:
         printf('data not found ')
    else:
     data1 = soup.find_all('img',{'class':'struct'})
     #print(soup)
     Formulai = soup.find_all('h1',{'id':'Top'})
     Formula = data[14].text
     Molecular_weight  = data[15].text
     IUPAC_Standard_InChI = data[16].text
     IUPAC_Standard_InChIKey = data[17].text
     CAS_Registry_Number = data[18].text
     Chemical_structure =  'Chemical_structure link click to view  : '+ 'https://webbook.nist.gov/'+ data1[0]['src']
     Isotopologues =data[20].text
     Other_names = data[21].text
     printf('Formula name : '+Formulai[0].text)
     printf(Formula)
     printf(Molecular_weight)
#     printf(IUPAC_Standard_InChI)
 #    printf(IUPAC_Standard_InChIKey)
#     printf(CAS_Registry_Number)
     printf(Chemical_structure)
     
#     printf(Isotopologues)
     printf(Other_names)
     printf('MORE INFORMATION : '+url)
     cho= inputf('----> ENTER FOR DOWNLOAD DATA (d/e) ')
     if 'd' in cho:
          file.file_write('data/data_.txt',Formulai[0].text,Formula,Molecular_weight,IUPAC_Standard_InChI,IUPAC_Standard_InChIKey,CAS_Registry_Number,Chemical_structure,Isotopologues,Other_names)
          
          
     else:
          pass
   except Exception as f:
         printf(f)
     
     
     
     
     
     



#https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Units=SI



head = {
"Host": "webbook.nist.gov",
"Connection": "keep-alive",
"Cache-Control": "max-age=0",
"DNT": "1",
"Save-Data": "on",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/999.999.99 (Linux; Android 10; USER) AppleWebKit/999999.9 (KHTML, like Gecko) Chrome/999.9...9.. Mobile Safari/99.99.999",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

"Sec-Fetch-Site": "none",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-User":"?1",
"Sec-Fetch-Dest": "document",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "si,en;q=0.9,en-US;q=0.8,en-GB;q=0.7",

}

def get_formula(url):
 try:
   req = requests.get(url)
   

   soup = bs4.BeautifulSoup(req.content.decode('utf-8'),'html.parser')

   a = soup.find_all("a")
  # print(req.url)
   img = soup.find_all('img')
   a_for = []
   
   for i in a:
     if '/cgi/cbook.cgi?ID=' in i['href']:
         a_for.append(i)
     else:
          pass

   co = 0
   try:
    for i in a_for:
     
     printf(str(co+1)+' : '+i.text+" :- "+img[co]['alt'])
     co += 1
   except:
       pass
  
   try:
    
    if not a_for:
        printf('formula data not found ')
    else:
     cho_ = int(inputf('Enter for number : '))
     link_for = 'https://webbook.nist.gov'+a_for[cho_-1]['href']
  #printf(link_for)
 # print(link_for)
     get_formula_det(link_for)
   except Exception as f:
       printf(f)
 except Exception as f:
      printf(f)
   

def main():
 os.system('clear')
 banner = """
\033[1;34m

█████████████████████████████████████████████
█▄─▄▄─█─▄▄─█▄─▄▄▀█▄─▀█▀─▄█▄─██─▄█▄─▄████▀▄─██
██─▄███─██─██─▄─▄██─█▄█─███─██─███─██▀██─▀─██
▀▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀
 
 """
 printf(banner)
 display = """

       1. Search for Species Data by Chemical Name [ carbon ]
       
       2. Search for Species Data by Chemical Formula [ EX :  o , h2o , h ]
       
       3. download data view 


"""
 printf(display)


 choice = inputf('Enter you are choice : ')
 if '1' in choice:
     printf("")
     name = inputf('Enter formula name : ')
     printf('')
     url = f"https://webbook.nist.gov/cgi/cbook.cgi?Name={name}&Units=SI"
     get_formula(url)
     
 elif '2' in choice:
     printf("")
     fo = inputf('Enter formula : ')
     url = f"https://webbook.nist.gov/cgi/cbook.cgi?Formula={fo}&NoIon=on&Units=SI"
     print('')
     get_formula(url)

 elif '3' in choice:
      file.data_view('data/data_.txt')


 else:
     printf('YOU ENTER CHOICE NOT FOUND ')

if __name__ == '__main__':
     main()

while True:
    a = inputf("  Do you want to go ahead? :> ")
    if a:
        exit()
    main()


     printf(str(co+1)+' : '+i.text+" :- "+img[co]['alt'])
     co += 1
   except:
       pass
  
   try:
    
    if not a_for:
        printf('formula data not found ')
    else:
     cho_ = int(inputf('Enter for number : '))
     link_for = 'https://webbook.nist.gov'+a_for[cho_-1]['href']
  #printf(link_for)
 # print(link_for)
     get_formula_det(link_for)
   except Exception as f:
       printf(f)
 except Exception as f:
      printf(f)
   

def main():
 os.system('clear')
 banner = """
\033[1;34m
████████████████████████████████████████
█▄─▄▄─█─▄▄─█▄─▄▄▀█▄─▀█▀─▄█▄─██─▄█▄─▄████▀▄─██
██─▄███─██─██─▄─▄██─█▄█─███─██─███─██▀██─▀─██
▀▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀
 
 """
 printf(banner)
 display = """

       1. Search for Species Data by Chemical Name [ carbon ]
       
       2. Search for Species Data by Chemical Formula [ EX :  o , h2o , h ]
       
       3. download data view 


"""
 printf(display)


 choice = inputf('Enter you are choice : ')
 if '1' in choice:
     printf("")
     name = inputf('Enter formula name : ')
     printf('')
