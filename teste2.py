import csv
import os
from time import sleep
from zipfile import ZipFile

import openpyxl

# Vendo os arquivos do teste1 dentro do zip:
with ZipFile('Teste1-downloads.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Desempacotando os zip do Teste1:
caminho = r'C:\Processo-Seletivo-IntutiveCare-Backend'
with ZipFile('Teste1-downloads.zip', 'r') as zip:
    for arquivo in os.listdir(caminho):
        zip.extractall('arquivo.desempacotado')

# Transformando a planilha em csv:
caminho2 = r'C:\Processo-Seletivo-IntutiveCare-Backend\arquivo.desempacotado\copy_of_Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537.xlsx'
print(caminho2)
excel = openpyxl.load_workbook(caminho2)
sheet = excel.active
arquivo = csv.writer(open("tabelaestruturada.csv",
                          'w',
                          encoding='utf-8',
                          )
                     )
for r in sheet.rows:
    arquivo.writerow([cell.value for cell in r])

sleep(3)

# Empacotando a planilha em csv:
arquivo = 'tabelaestruturada.csv'
with ZipFile('Teste_Álvaro_França_Fernandes.zip', 'w') as zip:
    zip.write('tabelaestruturada.csv')
