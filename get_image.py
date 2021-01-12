from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests

# navegador invisível
options = Options()
options.headless = True

# entrar no site
driver = webdriver.Firefox(options=options)
url = 'https://thispersondoesnotexist.com/image'
driver.get(url)
print('Entrou no Site')

# repetir 1000x e baixar as imagens
for i in range(1, 1001, 1):
    r = requests.get(url)
    with open('images/{}.jpg'.format(i), 'wb') as outfile:
        outfile.write(r.content)
    print('baixou: ', i)
    driver.get(url)
