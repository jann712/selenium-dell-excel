from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep

def navigationExecute(serialNumber, brand, name, driver):
    if brand == "ASUS":
        return 0
    
    notebookBrand = selectUrl(driver=driver, brand=brand)

    if (not notebookBrand == None): driver.get(notebookBrand)

    searchSerialNumber(serialNumber=serialNumber, brand=brand, driver=driver)
    return getNotebookInformation(name=name, serialNumber=serialNumber,brand=brand, driver=driver)

    # if (not driver.current_url.startswith("https://www.dell.com/support/home/en-us/product-support/servicetag/")):
    #     driver.get("https://www.dell.com/support/contractservices/en-us/")

    # #input serialnumber into searchbar
    # searchBar = driver.find_element(value='mh-search-input')
    # searchBar.send_keys(serialNumber)

    # #click on search
    # submitButton = driver.find_element(by='css selector', value='.mh-search-submit')
    # submitButton.click()

    # WebDriverWait(driver, 30).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')


    # #get notebook model
    # try:
    #     notebookModel = driver.find_element(by='css selector', value="h1[aria-label='SystemDescription']").text
    # except NoSuchElementException:
    #     driver.get("https://www.dell.com/support/contractservices/en-us/")
    #     return 0

    # #get warranty status
    # warranty = driver.find_element(by='css selector', value=".warrantyExpiringLabel").text

    # #treating warranty text
    # warranty = warranty.replace("Expires", "").replace("Expired", "").strip()

    # #print notebook model
    # print(f"\nN/S: {serialNumber[0]}")
    # print(f"Modelo: {notebookModel}")
    # print(f"Garantia: {warranty}")
    # print("=======================================================================")

    # # notebookDetails = {
    # #     'serialNumber': serialNumber,
    # #     'model': notebookModel,
    # #     'warranty': warranty
    # # }

    # return {
    #     'serialNumber': serialNumber[0],
    #     'model': notebookModel,
    #     'warranty': warranty
    # }

def selectUrl(brand, driver):
    if brand == "DELL":
        # if driver.current_url.startswith("https://www.dell.com/support/home/en-us/product-support/servicetag/"):
        if driver.current_url.startswith("https://www.dell.com"):
            # return "https://www.dell.com/support/contractservices/en-us/"
            return None

        else: return "https://www.dell.com/support/contractservices/en-us/"

    elif brand == "LENOVO":
        if driver.current_url.startswith("https://pcsupport.lenovo.com/br/pt/products/laptops-and-netbooks/"):
            return None

        else: return "https://pcsupport.lenovo.com/br/pt/warranty-lookup/#/"

    # elif brand == "ASUS":
    #     if driver.current_url.startswith("https://www.asus.com/"):
    #         return None 
    #     else: return "https://www.asus.com/support/warranty-status-inquiry/"

def searchSerialNumber(serialNumber, brand, driver):
    if brand == "DELL":
        
            
        if driver.current_url == "https://www.dell.com/support/contractservices/en-us/":
            try:
                currentCountryButton = driver.find_element(By.ID, value='btn_ooc-current-country')
                currentCountryButton.click()
            except NoSuchElementException: pass
        
        searchBar = driver.find_element(By.CLASS_NAME, value='mh-search-input') 
        searchBar.clear() 
        searchBar.send_keys(serialNumber)
        submitButton = driver.find_element(By.CLASS_NAME, value='mh-search-submit')
            
        #input serialnumber into searchbar

        

        #click on search
        
        
        try:
            submitButton.click()
        
        except ElementClickInterceptedException:
            sleep(4)
            noButton = driver.find_element(By.CLASS_NAME, value="noButton buttons")
            noButton.click()
            # sleep(1)
            # newSubmitButton = driver.find_element(by='css selector', value='.mh-search-submit')
            # newSubmitButton.click()
            submitButton.click()
            
                
        
        sleep(5)
            
                

        # WebDriverWait(driver, 30).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        return

    elif brand == "LENOVO":
        #input serialnumber into searchbar
        if driver.current_url.startswith("https://pcsupport.lenovo.com/br/pt/products/laptops-and-netbooks"):
            searchBar = driver.find_element(By.CSS_SELECTOR, value="input[placeholder='Buscar Suporte PC']")
            # submitButton = driver.find_element(By.CLASS_NAME, value="sn-title-icon inputing icon-l-right inputmode")
            
        else: 
            searchBar = driver.find_element(By.CLASS_NAME,'button-placeholder__input')
            # submitButton = driver.find_element(By.CLASS_NAME,"basic-search")
               
        searchBar.clear()
        searchBar.send_keys(serialNumber)
        sleep(1)
        searchBar.send_keys(Keys.ENTER)
        

        #click on search
        # submitButton = driver.find_element_by(by='css selector', value="button[class='basic-search__suffix-btn btn btn-primary']")
        
        # submitButton.click()

        WebDriverWait(driver, 30).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        return
    # elif brand == "ASUS":
    #     return


def getNotebookInformation(name, serialNumber, brand, driver):
    if brand == "DELL":
        
        
        try:
            notebookModel = driver.find_element(by='css selector', value="h1[aria-label='SystemDescription']").text
        except NoSuchElementException:
            # driver.get("https://www.dell.com/support/contractservices/en-us/")
            return 0

        
        # serialNumber =  driver.find_element(By.CLASS_NAME,"service-tag mb-0").text
        
        #get warranty status
        warranty = driver.find_element(By.CSS_SELECTOR, value=".warrantyExpiringLabel").text

        #treating warranty text
        warranty = warranty.replace("Expires", "").replace("Expired", "").strip()

         
        data = {
        'name': name,
        'serialNumber': serialNumber,
        'model': notebookModel,
        'warranty': warranty,
        'odd': False
        }
        
        # sleep(8)
        
        # try:
        #     noButton = driver.find_element(by="id", value="noButtonIPDell")
        #     noButton.click()
            
        # except NoSuchElementException: pass
        #     # print("No button found!")
        
        if not driver.current_url.startswith("https://www.dell.com/support/home/en-us/product-support/servicetag"):
            searchBar = driver.find_element(By.CLASS_NAME, value='mh-search-input')
            searchBar.clear()
            data['odd'] = True
        #print notebook model
        print(f"Nome: {name}")
        print(f"N/S: {serialNumber}")
        print(f"Modelo: {notebookModel}")
        print(f"Garantia: {warranty}")
        print("=======================================================================")

        
        
        return data


    if brand == "LENOVO":
        try:
            sleep(10)
            modelDiv = driver.find_element(By.CLASS_NAME, "prod-name")
            notebookModel = modelDiv.find_element(By.TAG_NAME, "h4").text
            # notebookModel = driver.find_element(by='css selector', value="h1[aria-label='SystemDescription']").text
        except NoSuchElementException:
            # driver.get("https://www.dell.com/support/contractservices/en-us/")
            return 0

        #get warranty status
        warranty = driver.find_element(By.CLASS_NAME,"property-value").text

        #treating warranty text
        # warranty = warranty.replace("Expires", "").replace("Expired", "").strip()
        data = {
        'name': name,
        'serialNumber': serialNumber,
        'model': notebookModel,
        'warranty': warranty,
        'odd': False
        }
        #print notebook model
        print(f"Nome: {name}")
        print(f"N/S: {serialNumber}")
        print(f"Modelo: {notebookModel}")
        print(f"Garantia: {warranty}")
        print("=======================================================================")

        return data
          
    # elementInformation = {
    #     # "searchBar": {
    #     #     "element": "",
    #     #     "button": ""
    #     # },
    #     "notebook": {
    #         "model": "",
    #         "warranty": ""
    #     }
    # }





