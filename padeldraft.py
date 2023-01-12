# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

from datetime import datetime
import random

dayofweek = datetime.now().weekday()


def draft():  # função para fazer o sorteio. Deve ser chamada à quarta-feira às 20h
    players = open("list.txt").readlines()
    random.shuffle(players)
    player_1 = players.pop()
    random.shuffle(players)
    player_2 = players.pop()
    random.shuffle(players)
    player_3 = players.pop()
    random.shuffle(players)
    player_4 = players.pop()

    print("\nplayers for upcoming game are:")
    print(player_1+"\n", player_2+"\n", player_3+"\n", player_4+"\n")


def salutation():
    return ("Hi welcome!")


def draftlist_reseter():  # função para apagar toda a informação do ficheiro de suporte, para o novo sorteio. Deve ser chamada no mesmo dia que o sorteio, depois às 21h
    with open("list.txt", "r+") as draftlist:
        draftlist.truncate(0)  # need '0' when using r+


# função que verifica se o jogador já se inscreveu e o adiciona à lista caso ainda não o tenha feito. Só pode estar aberto entre segunda e quarta-feira
def draftlist_verifier(player):
    with open('list.txt', "r+") as draftlist:
        if player in draftlist.read():
            # if player in players:
            print("name already listed")
            return False
        elif player == "erase":
            draftlist_reseter()
        else:
            draftlist.write(player + "\n")
            return True


def timeframe_verifier():
   # aqui especificamos que a inscrição só pode ser feita até quarta-feira (dia 2 da semana)
    if 2 <= dayofweek <= 3 and datetime.now().hour < 20:
        # Proposta é abrir inscrições entre 4ª (dia 2) e 5ª (dia 3)
        for x in range(0, 6):
            player = input("Enter your name for the draft:")
            return player
            draftlist_verifier(player)
    else:
        print("draft already ended")
        return ("draft already ended")

    if dayofweek == 3 and datetime.now().hour == 20:
        draft()


def timeframe_verifier_2():
   # aqui especificamos que a inscrição só pode ser feita até quarta-feira (dia 2 da semana)
    if 2 <= dayofweek <= 4 and datetime.now().hour < 20:
        # Proposta é abrir inscrições entre 4ª (dia 2) e 5ª (dia 3)
        return (True)
    else:
        print("draft already ended")
        return (False)


if __name__ == '__main__':
    timeframe_verifier()
