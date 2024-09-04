from selenium import webdriver
from functions import navigationExecute
from time import sleep
import csv
import xlsxwriter

#criar pasta de trabalho e planilha
workbook = xlsxwriter.Workbook('notebooks_dell.xlsx')
worksheet = workbook.add_worksheet()

#instanciar as opções do webdriver
options = webdriver.FirefoxOptions()
options.accept_insecure_certs = True
options.add_argument("--incognito")

#instanciar o webdriver
driver = webdriver.Firefox(options=options)


#link da dell para verificar os dados do modelo
# driver.get("https://www.dell.com/support/contractservices/en-us/")


#set wait time
driver.implicitly_wait(5)

#click on keep the current country
# currentCountryButton = driver.find_element(value='btn_ooc-current-country')
# currentCountryButton.click()

#ler o csv
# csv.register_dialect(dialect='dialect', delimiter=';')
with open('serialNumbers.csv', newline='') as csvfile:
    #começar a escrita pela celula A1, coluna 1, linha 1. a indexação começa no 0
    row = 0
    col = 0
    
    #iniciar o leitor csv
    reader = csv.reader(csvfile, delimiter=";")

    next(reader)
    #escrever na planilha excel
    for line in reader:
        # print(line)
        #executar a função com a navegação do selenium
        notebookDetails = navigationExecute(brand=line[2],serialNumber=line[1], name=line[0], driver=driver)

        #caso não tenha correspondência no site da dell, irá para a próxima linha
        if notebookDetails == 0: continue

        #escrever para a planilha, com os dados obtidos pelo selenium
        worksheet.write_row(row=row, col=col,data=list(notebookDetails.values()), cell_format=None)
        row += 1

        #aguardar 3 segundos
        sleep(3)
        


#concluir planilha excel
workbook.close()

#fechar "navegador"
driver.quit()



