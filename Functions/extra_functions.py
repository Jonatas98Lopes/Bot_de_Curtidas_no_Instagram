from time import sleep
from random import randint

def pausar():
    """
    Pausa a execução do programa de 3 à 10 segundos aleatoriamente.


    A função não recebe nenhum argumento.
    """
    sleep(randint(2, 5))

def repousar():
    """
    Pausar a execução do programa de 30 à 60 segundos aleatoriamente.

    A função não recebe nenhum argumento.
    """
    sleep(randint(30, 60))

def digitar_naturalmente(texto, elemento):
    """
    Digita um texto de forma semelhante a um ser humano.

    Recebe o texto e o elemento onde deseja digitar.
    """
    for letra in texto:
        elemento.send_keys(letra)
        sleep(randint(1,5)/30)







