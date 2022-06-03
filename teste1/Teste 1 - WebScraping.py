import os
from pathlib import Path
from time import sleep
from zipfile import ZipFile

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent.parent.parent.parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / \
    'Processo-Seletivo-IntutiveCare-Backend' / 'bin' / 'chromedriver.exe'


# Opções de download, mude apenas o "download.default_directory
options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Processo-Seletivo-IntutiveCare-Backend\Teste1-dowloads",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    "plugins.always_open_pdf_externally": True})

# Opções de download, mude apenas o "download.default_directory


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_experimental_option("prefs", {
                "download.default_directory": r"C:\Processo-Seletivo-IntutiveCare-Backend\Teste1-dowloads",
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True,
                "plugins.always_open_pdf_externally": True})

    chrome_service = Service(
        executable_path=CHROME_DRIVER_PATH,
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    # Example
    options = ('--disable-gpu', '--no-sandbox',)
    browser = make_chrome_browser(*options)

    def url():
        browser = make_chrome_browser(*options)
    browser.get('https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude')
    browser.find_element_by_xpath(
        "/html/body/div[3]/div[1]/main/div[2]/div/div[4]/div/p[11]/a").click()

    browser.find_element_by_xpath(
        "/html/body/div[3]/div[1]/main/div[2]/div/div[4]/div/p[12]/a").click()
    browser.find_element_by_xpath(
        "/html/body/div[3]/div[1]/main/div[2]/div/div[4]/div/p[13]/a").click()
    browser.find_element_by_xpath(
        "/html/body/div[3]/div[1]/main/div[2]/div/div[4]/div/p[14]/a").click()

    browser.find_element_by_xpath(
        "/html/body/div[3]/div[1]/main/div[2]/div/div[4]/div/p[15]/a").click()
sleep(3)

# Empacotando os downloads
caminho = r'C:\Processo-Seletivo-IntutiveCare-Backend\Teste1-dowloads'
with ZipFile('Teste1-downloads.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)
