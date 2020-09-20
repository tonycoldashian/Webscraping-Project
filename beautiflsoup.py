import bs4,requests
def getflipkartprice(producturl):
    res = requests.get(producturl)
    if res.status_code== False:
        return print ("Error Downloading URL")
    else:
        soup = bs4.BeautifulSoup(res.text,'html.parser')
        elems = soup.select('._1vC4OE')
        availability=soup.select('._1S11PY')
        return (elems[0].text.strip())

def getavail(url):
    res = requests.get(url)
    if res.status_code== False:
        return print ("Error Downloading URL")
    else:
        soup = bs4.BeautifulSoup(res.text,'html.parser')
        availability=soup.select('._1S11PY')
        print(type(availability))
        return (availability[0].text.strip())

pricelist=[] 
file = open("/home/aswyn/Downloads/laptopurl.txt",'r')
linenum= int(input("Enter Number of Laptops you want to check :"))
for price in range(1,linenum+1):
    url = file.readline()
    price = getflipkartprice(url)
    #status = getavail(url)
    pricelist.append(price)
    print(url,end='')
    print ("Price :"+price +"\n")

pricelist.sort()
for i in range(linenum):
    print(pricelist[i])
print('Lowest Price among them is: '+str(pricelist[0]))
file.close()