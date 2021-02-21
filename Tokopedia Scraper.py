import bs4
import time
from selenium import webdriver
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


chrome_path = 'chromedriver_win32/chromedriver'

driver = webdriver.Chrome(chrome_path)

keyword = "gtx 1660 super"

filename = "Scraping Result/tokopedia_" + keyword +".txt"
f = open(filename, "w", encoding="utf-8")
f.write("Tokopedia Ads" + "\t" + "URL" + "\t" + "Product Name" + "\t" + "Product Sold" + "\t" + "Price" + "\n") 

#opening webpage
num_products = 0
for page in range(1,100):
    myurl = f'https://www.tokopedia.com/search?navsource=home&page={page}&q=gtx%201660%20super&st=product'
    buka = driver.get(myurl)
    scroll_pause_time = 0.1
    screen_height = driver.execute_script("return window.screen.height;")
    i = 1
    while True:
        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            break
    
    page_source = driver.page_source
    soup_this = soup(page_source, "html.parser")
    
    products = soup_this.find_all('div', class_='css-1g20a2m')
    
    for product in products:
        
        ads = product.find('div', class_='css-14x6rma')
        ads = f"{ads}"
        ads = ads.replace('<div class="css-14x6rma"><span class="css-1tbvbqz" data-testid="divSRPTopadsIcon">',"")
        ads = ads.replace('</div>',"")
        ads = ads.replace('</span>',"")
        f.write(f"{ads}" + "\t")
        
        product_url = product.find('a', href=True)
        f.write(product_url['href'] + "\t")
        
        product_name = product.find('div', class_='css-18c4yhp')
        product_name = f"{product_name}"
        product_name = product_name.replace('<div class="css-18c4yhp" data-testid="spnSRPProdName">',"")
        product_name = product_name.replace('</div>',"")
        f.write(f"{product_name}" + "\t")
        
        product_sold = product.find('span', class_='css-1mv2cn2')
        product_sold = f"{product_sold}"
        product_sold = product_sold.replace('<span class="css-1mv2cn2">',"")
        product_sold = product_sold.replace('</span>',"")
        product_sold = product_sold.replace('Terjual ',"")
        
        if product_sold.find(",") == 1:
            product_sold = product_sold.replace(',',"")
            product_sold = product_sold.replace(' rb',"")
            product_sold = int(product_sold)*100
            product_sold = str(product_sold)
        else:
            product_sold = product_sold.replace(' rb',"000")
            product_sold = product_sold.replace('None',"0")
            
        f.write(f"{product_sold}" + "\t")
        
        price = product.find('div', class_='css-rhd610')
        price = f"{price}"
        price = price.replace('<div class="css-rhd610" data-testid="spnSRPProdPrice">',"")
        price = price.replace('</div>',"")
        price = price.replace('Rp',"")
        price = price.replace('.',"")
        f.write(f"{price}" + "\n")
        
    num_products = num_products + len(products)
        
    print(f"Page-{page}, Products Detected: {len(products)}, Total Products Detected: {num_products}")


f.close()
driver.close()