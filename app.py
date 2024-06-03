# Importando as bibliotecas utilizadas durante o código
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Caminho do arquivo .csv para utilizarmos depois
file_path = './informacoes.csv'

# Inicializando as variáveis com informações úteis de cadastro
username = ''
password = ''
first_name = ''
last_name = ''
postal_code = ''

# Lendo o arquivo .csv e guardando o conteúdo dele nas variáveis declaradas anteriormente
with open(file_path, mode='r', newline='') as file:
    csv_reader = csv.DictReader(file, delimiter=';')
    first_row = next(csv_reader)
    
    username = first_row['username']
    password = first_row['password']
    first_name = first_row['first name']
    last_name = first_row['last name']
    postal_code = first_row['postal code']


# Configurações de driver e do selenium para podermos utilizar o navegador Google Chrome sem problemas
chrome_op = Options()
chrome_op.add_experimental_option('detach', True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_op)

# Acessando a URL do Swag Labs
driver.get('https://www.saucedemo.com/')

# Preenchendo o formulário de login da página e, em seguida, clicando no botão de login.
driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

# Pegando o XPATH do botão de "adicionar ao carrinho" de cada item que desejamos comprar e armazenando em variáveis
camisa_vermelha = driver.find_element(By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
camisa_preta = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
luz_bicicleta = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')

# Adicionando os itens desejados no carrinho, ou seja, clicando no botão
camisa_vermelha.click()
camisa_preta.click()
luz_bicicleta.click()

# Armazenando o XPATH do botão de carrinho de compras e clicando no mesmo
carrinho_de_compras = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
carrinho_de_compras.click()

# Armazenando o XPATH do botão de checkout e clicando em seguida
botao_checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
botao_checkout.click()

# Preenchendo o formulário relacionado ao remetende da entrega com os dados recolhidos anteriormente no arquivo .csv
driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys(first_name)
driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys(last_name)
driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys(postal_code)

# Armazenando o XPATH do botão para continuar o ato da compra e clicando no mesmo
botao_continue = driver.find_element(By.XPATH, '//*[@id="continue"]')
botao_continue.click()

# Armazenando na variável "valor_total" o texto como o valor total da compra que está sendo realizada
valor_total = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]').text

# Armazenando o XPATH do botão para finalizar a compra e, depois, clicando nele
botao_finalizar_compra = driver.find_element(By.XPATH, '//*[@id="finish"]')
botao_finalizar_compra.click()

# Printando no console o valor total da compra
print(valor_total)

# Após realizar todo o procedimento, fecharemos a aba do navegador que foi utilizada
driver.close()