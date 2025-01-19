from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Função para configurar o driver com opções para melhorar o carregamento
def setup_driver():
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--headless")  # Roda em modo headless
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-images")  # Desabilita as imagens
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)  # Adiciona um tempo de espera implícita para os elementos
    return driver

# Função para fazer o scraping
def get_producao_scraping():
    driver = setup_driver()
    driver.set_page_load_timeout(30)  # Aumenta o timeout para 30 segundos
    
    try:
        driver.get('http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02')
    except TimeoutException:
        print("A página demorou muito para carregar, continuando...")
    try:
        # Esperar até o elemento estar disponível
        iframe = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/table[4]/tbody/tr/td[2]/div/div/table[2]/tbody/tr/td[1]/a/span'))
        )
        # Scroll até o iframe e clicar
        ActionChains(driver).scroll_to_element(iframe).perform()
        iframe.click()

        # Aguarde mais alguns segundos para garantir que a página foi carregada
        time.sleep(5)

        data = {"mensagem": "Dados de produção coletados com sucesso"}
    except TimeoutException:
        print("O iframe não foi encontrado ou demorou demais para carregar.")
        data = {"mensagem": "Falha ao coletar os dados"}

    driver.quit()
    return data



# Função para fazer o scraping
def get_processamento_scraping():
    driver = setup_driver()
    driver.set_page_load_timeout(30)  # Aumenta o timeout para 30 segundos
    
    try:
        driver.get('http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03')
    except TimeoutException:
        print("A página demorou muito para carregar, continuando...")
    try:
        # Esperar até o elemento estar disponível
        iframe = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/table[4]/tbody/tr/td[2]/div/div/table[2]/tbody/tr/td[1]/a/span'))
        )
        # Scroll até o iframe e clicar
        ActionChains(driver).scroll_to_element(iframe).perform()
        iframe.click()

        # Aguarde mais alguns segundos para garantir que a página foi carregada
        time.sleep(5)

        data = {"mensagem": "Dados de processamento coletados com sucesso"}
    except TimeoutException:
        print("O iframe não foi encontrado ou demorou demais para carregar.")
        data = {"mensagem": "Falha ao coletar os dados"}

    driver.quit()
    return data




# Função para fazer o scraping
def get_comercializacao_scraping():
    driver = setup_driver()
    driver.set_page_load_timeout(30)  # Aumenta o timeout para 30 segundos
    
    try:
        driver.get('http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04')
    except TimeoutException:
        print("A página demorou muito para carregar, continuando...")
    try:
        # Esperar até o elemento estar disponível
        iframe = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/table[4]/tbody/tr/td[2]/div/div/table[2]/tbody/tr/td[1]/a/span'))
        )
        # Scroll até o iframe e clicar
        ActionChains(driver).scroll_to_element(iframe).perform()
        iframe.click()

        # Aguarde mais alguns segundos para garantir que a página foi carregada
        time.sleep(5)

        data = {"mensagem": "Dados de Comercialização coletados com sucesso"}
    except TimeoutException:
        print("O iframe não foi encontrado ou demorou demais para carregar.")
        data = {"mensagem": "Falha ao coletar os dados"}

    driver.quit()
    return data



def get_importacao_scraping():
    driver = setup_driver()
    driver.set_page_load_timeout(30)  
    
    try:
        driver.get('http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05')
    except TimeoutException:
        print("A página demorou muito para carregar, continuando...")
    try:
        iframe = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/table[4]/tbody/tr/td[2]/div/div/table[2]/tbody/tr/td[1]/a/span'))
        )
        ActionChains(driver).scroll_to_element(iframe).perform()
        iframe.click()

        time.sleep(5)

        data = {"mensagem": "Dados de importação coletados com sucesso"}
    except TimeoutException:
        print("O iframe não foi encontrado ou demorou demais para carregar.")
        data = {"mensagem": "Falha ao coletar os dados"}

    driver.quit()
    return data


def get_exportacao_scraping():
    driver = setup_driver()
    driver.set_page_load_timeout(30)  
    
    try:
        driver.get('http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06')
    except TimeoutException:
        print("A página demorou muito para carregar, continuando...")
    try:
        iframe = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/table[4]/tbody/tr/td[2]/div/div/table[2]/tbody/tr/td[1]/a/span'))
        )
        ActionChains(driver).scroll_to_element(iframe).perform()
        iframe.click()

        time.sleep(5)

        data = {"mensagem": "Dados de exportação coletados com sucesso"}
    except TimeoutException:
        print("O iframe não foi encontrado ou demorou demais para carregar.")
        data = {"mensagem": "Falha ao coletar os dados"}

    driver.quit()
    return data



    
