from Functions.extra_functions import *
from Interfaces.usuario import DadosUsuario
from Interfaces.erro import Erro
from Interfaces.fim import Fim
from selenium.common.exceptions import StaleElementReferenceException
from Functions.inicializar import GoogleChrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from random import randint



def interagir_com_elemento_instavel(texto, xpath):
    try:
        campo_comentario = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,xpath)))
        pausar()
        campo_comentario.send_keys(texto)
    except StaleElementReferenceException:
        interagir_com_elemento_instavel(texto, xpath)



usuario = DadosUsuario()
# 1. RECEBER O NOME DE USUÁRIO NO INSTAGRAM.
nome_usuario = usuario.values["user_name"]
#2. RECEBER A SENHA DO INSTAGRAM.
senha = usuario.values["password"]
# # 3. RECEBER O NOME DA PÁGINA QUE DESEJA MONITORAR.
pagina = usuario.values["page"]
# # 4. RECEBER O COMENTÁRIO PADRÃO.
comentario = usuario.values["comment"]


if usuario.button == "Enviar":
    # 5. ABRIR O NAVEGADOR
    try:
        browser = GoogleChrome()
    except:
        erro = Erro(mensagem='Ops! Houve algum problema ao abrir o navegador.', titulo='Erro de inicialização:')
    else:
        driver = browser.get_driver()
        wait = browser.get_wait()
        # 6. ACESSAR O SITE: https://www.instagram.com/
        driver.get('https://www.instagram.com/')
        # 7. ESPERAR A PÁGINA CARREGAR
        repousar()
        while True:
            # 8. LOCALIZAR O CAMPO DE NOME DE USUÁRIO
            campo_usuario = wait.until(expected_conditions.element_to_be_clickable((By.NAME, 'username')))
            pausar()
            # 9. DIGITAR O NOME DE USUÁRIO.
            digitar_naturalmente(nome_usuario, campo_usuario)
            # 10. LOCALIZAR O CAMPO DE SENHA.
            campo_senha = wait.until(expected_conditions.element_to_be_clickable((By.NAME, 'password')))
            pausar()
            # 11. DIGITAR A SENHA DO USUÁRIO.
            digitar_naturalmente(senha, campo_senha)
            # 12. LOCALIZAR O BOTÃO "Entrar".
            botao = driver.find_element(By.XPATH, '//button[@type="submit"]')
            pausar()
            # 13. CLICAR NO BOTÃO ENTRAR.
            botao.click()
            # 14. ESPERAR A PÁGINA CARREGAR.        
            repousar()
            try:
                dados_incorretos = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//p[text()="Sua senha está incorreta. Confira-a."]')))
            except:
                # 15. ACESSAR A PÁGINA: https://www.instagram.com/NOMEDAPÁGINA/
                driver.get(f'https://www.instagram.com/{pagina}')
                # 16. ESPERAR A PÁGINA CARREGAR.
                repousar()
                try:
                    pagina_nao_existente = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//span[@class="x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye x133cpev x1s688f x5n08af x2b8uid x4zkp8e x41vudc x10wh9bi x1wdrske x8viiok x18hxmgj"]')))
                except:
                    # 17. LOCALIZAR O POST MAIS RECENTE.
                    posts = wait.until(expected_conditions.visibility_of_any_elements_located((By.XPATH, '//div[@class="_aagu"]')))
                    pausar()
                    # 18. CLICAR NO POST MAIS RECENTE.
                    posts[0].click()
                    pausar()
                    # 19. ESPERAR A PÁGINA CARREGAR.
                    repousar()
                    try:
                    # 20. LOCALIZAR O ÍCONE DE CURTIR.
                        icone_curtir = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Descurtir"]')))

                    #CASO A FOTO NÃO ESTEJA CURTIDA:
                    except:
                        icone_curtir = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Curtir"]')))
                        pausar()
                        # 21. CLICAR NO ÍCONE DE CURTIR
                        icone_curtir.click()
                        pausar()
                        # 22. LOCALIZAR O CAMPO DE COMENTÁRIO.
                        # 23. DIGITAR O COMENTÁRIO PADRÃO NO CAMPO DE COMENTÁRIO.
                        interagir_com_elemento_instavel(comentario, '//textarea[@aria-label="Adicione um comentário..."]')
                        pausar()
                        # 24. LOCALIZAR O BOTÃO "Publicar".
                        botao_publicar = driver.find_element(By.XPATH, '//div[@class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1i0vuye x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37"]')
                        pausar()
                        # 25. CLICAR NO BOTÃO "Publicar".
                        botao_publicar.click()

                        # 26. ESPERAR O POST SER PUBLICADO.
                        repousar()
                    # 27. ACESSAR A PÁGINA: https://www.instagram.com/
                    driver.get('https://www.instagram.com/')
                    repousar()
                    # 28. LOCALIZAR O ÍCONE DE FOTO DO USUÁRIO À ESQUERDA.
                    icone_perfil = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//div[@class="x9f619 xxk0z11 xii2z7h x11xpdln x19c4wfv xvy4d1p"]/span')))
                    pausar()
                    # 29. CLICAR NELE.
                    icone_perfil.click()
                    # 30. ESPERAR A PÁGINA CARREGAR.
                    repousar()
                    # 31. LOCALIZAR O ÍCONE DE ENGRENAGEM
                    icone_configuracoes = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//div[@role="button"]')))
                    pausar()
                    # 32. CLICAR NELE.
                    icone_configuracoes.click()
                    pausar()
                    # 33. LOCALIZAR O BOTÃO "Sair".
                    botao_sair = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//button[text()="Sair"]')))
                    pausar()
                    # 34. CLICAR NELE.
                    botao_sair.click()
                    # 35. ESPERAR A PÁGINA CARREGAR.
                    fim = Fim()
                    sleep(randint(86400, 108000))
                else:
                    driver.quit()
                    erro = Erro(mensagem='Ops! Parece que a página informada não existe.', titulo='Página não encontrada:')
            else:
                driver.quit()
                erro = Erro(mensagem='Ops! Parece que seu nome de usuário ou senha estão errados.', titulo='Erro nas credenciais de acesso:')