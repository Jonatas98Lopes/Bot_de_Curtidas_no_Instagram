# Bot_de_Curtidas_no_Instagram

***

## Descrição:

Neste projeto, vamos monitorar a curtida do post mais recente de uma página. Se o post mais recente não estiver curtido, vamos curtí-lo e adicionar um comentário padrão.

***

## Requisitos:

* Ter o Python 3 instalado no seu computador. De preferência, na versão 3.11.

* Ter habilitado a opção **Add to Path** na hora da instalação do Python.

* Possuir o navegador Google Chrome instalado.

* Possuir uma resolução de tela de **1366 x 766**. É possível alterar essas configurações no seu sistema operacional. No Windows, por exemplo, procure por Configurações de exibição. 

* Ter o perfil do Instagram em português brasileiro.

Assista ao vídeo de funcionamento do projeto [clicando aqui!](https://www.linkedin.com/feed/update/urn:li:ugcPost:7092271532390907904/)

***

## Algoritmo do Projeto:

1. Receber o nome de usuário no Instagram.
2. Receber a senha do Instagram.
3. Receber o nome da página que deseja monitorar.
4. Receber o comentário padrão.
5. Abrir o navegador.
6. Acessar o site: https://www.instagram.com/
7. Esperar a página carregar.
A CADA 24 HORAS, DEVEMOS:
    8. Localizar o campo de nome de usuário.
    9. Digitar o nome de usuário.
    10. Localizar o campo de senha.
    11. Digitar a senha do usuário.
    12. Localizar o botão "Entrar".
    13. Clicar no botão "Entrar".
    14. Esperar a página carregar.
    15. Acessar a página: https://www.instagram.com/NOMEDAPÁGINA/
    16. Esperar a página carregar.
    17. Localizar o post mais recente.
    18. Clicar no post mais recente.
    19. Esperar a página carregar.
    20. Localizar o ícone de curtir.
    CASO A FOTO NÃO ESTEJA CURTIDA:
        21. Clicar no ícone de curtir.
        22. Localizar o campo de comentário.
        23. Digitar o comentário padrão no campo de comentário.
        24. Localizar o botão "Publicar".
        25. Clicar no botão "Publicar".
        26. Esperar o post ser publicado.
    27. Acessar a página: https://www.instagram.com/
    28. Localizar o ícone de foto de usuário à esquerda.
    29. Clicar nele.
    30. Esperar a página carregar.
    31. Localizar o ícone de configurações
    32. Clicar nele.
    33. Localizar o botão "Sair".
    34. Clicar nele.
    35. Parar por, pelo menos, 24 horas.

***

## Como rodar o projeto?

Assim que clonar este código, sugiro que você crie um ambiente virtual isolando os arquivos que estão no seu computador do diretório do projeto.

### Criando ambiente virtual com Python:

1. Clone o projeto.

2. Estando dentro da pasta do projeto, abra o seu terminal.

CASO ESTEJA NO **WINDOWS**, RODE O COMANDO ABAIXO E AGUARDE A CRIAÇÃO:

```
python -m venv nome_do_ambiente_virtual
```

**nome_do_ambiente_virtual**: Defina o nome do seu ambiente virtual.

CASO ESTEJA NO LINUX OU NO MAC, RODE O COMANDO ABAIXO E A AGUARDE A CRIAÇÃO:

```
python3 -m venv nome_do_ambiente_virtual
```
**nome_do_ambiente_virtual**: Defina o nome do seu ambiente virtual.

3. Ative o ambiente virtual através do seu terminal:

NO CASO DO **WINDOWS**, RODE:
```
nome_do_ambiente_virtual\Scripts\activate
```
**nome_do_ambiente_virtual**: Coloque o nome que definiu na criação do ambiente virtual.

NO CASO DO **LINUX** OU **MAC**, RODE:

```
source nome_do_ambiente_virtual\bin\activate
```
**nome_do_ambiente_virtual**: Coloque o nome que definiu na criação do ambiente virtual.

***

### Instalando bibliotecas necessárias:

Feito isso, vamos instalar as bibliotecas necessárias através do arquivo requirements.txt:
No **Windows**, estando dentro da pasta do projeto e com o ambiente virtual ativado, rode:

```
pip install -r requirements.txt
```
No **Linux** ou **MAC**, estando dentro da pasta do projeto e com o ambiente virtual ativado, rode:

```
pip3 install -r requirements.txt
```
Pronto! Você está apto para rodar o projeto.

***

### Gerando executável:

Caso você queira um executável do projeto. Você deve ter executado as etapas anteriores. - ATÉ A PARTE DE INSTALAR AS BIBLIOTECAS DO ARQUIVO requirements.txt.

Feito isso, você deve estar com o seu ambiente virtual ativado e abrir o seu terminal na pasta raiz do projeto.

Estando lá, digite o seguinte comando

NO **WINDOWS**:
```
python setup.py build
```

NO **LINUX** OU NO **MAC**:
```
python3 setup.py build
```

Uma pasta **build**, com um arquivo **app** deve ser gerado.
O ARQUIVO **app** será o seu executável.