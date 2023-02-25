# Para realizar essa automação , você precisa das Bibliotecas 
# Playawright e Time
#https://playwright.dev/ acesso o site para que possa ler os documetos da biblioteca 

from playwright.sync_api import  sync_playwright
import time 



# Aqui foi escolhido  o Google Chrome para realizar o prpcedimento 
with sync_playwright () as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    
    
    # Digite o link que irá começar o processo 
    pagina.goto("https://www.google.com/")


    # Para localizar um setor de uma página você precisa usar o .locator e o Xpath do local escolhido 
    # Lembrando que o wait_for_timeout é usado para dar um tempo determinado para que as páginas abram sem que acha erro no processo 
    pagina.locator('xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').click()
    pagina.wait_for_timeout(1000)
    
    pagina.fill('xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input ' , ' vip central do assinante')
    pagina.wait_for_timeout(1000)
    
    pagina.locator('xpath=/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]').click()
    pagina.wait_for_timeout(1000)

    pagina.locator('xpath=//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a/h3').click()
    pagina.wait_for_timeout(1000)

    pagina.locator('xpath=//*[@id="__next"]/div[4]/div[4]/div/ul/li[9]/button').click()
    pagina.wait_for_timeout(8000)
    
    # Para preencher um setor do tipo input de uma página você precisa usar o .fill e o Xpath do local escolhido
    pagina.fill('xpath=//*[@id="username"]' , 'Digite seu CPF')
    pagina.wait_for_timeout(1000)
    
   
    pagina.fill('xpath=//*[@id="password"]' , 'Digite sua Senha')
    pagina.wait_for_timeout(1000)

    pagina.locator('xpath=//*[@id="kc-login"]').click()
    pagina.wait_for_timeout(8000)

    pagina.locator('xpath=//*[@id="root"]/div[1]/div/div/div/div/p[2]').click()
    pagina.wait_for_timeout(5000)

    pagina.locator('xpath=//*[@id="root"]/div[1]/main/div[1]/div[1]/div[2]/div[1]/div/div/div[1]/a').click()
    pagina.wait_for_timeout(1000)

    pagina.locator('xpath=//*[@id="root"]/div[1]/div/div[2]/div[2]/div[2]/span[2]/img').click()
    pagina.wait_for_timeout(1000)


    pagina.locator('xpath=//*[@id="root"]/div[3]/div[1]/div/form/div[2]/button').click()
    pagina.wait_for_timeout(1000)


    # time.sleep (coloque o tempo que a página precisa ficar aberta até que automação seja realizada )
    time.sleep(1000)


