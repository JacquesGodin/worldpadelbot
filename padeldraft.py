from datetime import datetime
import random

dayofweek = datetime.now().weekday()


def draft():  # function to randomly pick 4 players from the list of players
    players = open("list_players.txt").readlines()
    random.shuffle(players)
    player_1 = players.pop()
    random.shuffle(players)
    player_2 = players.pop()
    random.shuffle(players)
    player_3 = players.pop()
    random.shuffle(players)
    player_4 = players.pop()

    match = [player_1, player_2, player_3, player_4]
    return (match)


def draftlist_reseter():  # erases all the entries in the list_players.txt
    with open("list_players.txt", "r+") as draftlist:
        draftlist.truncate(0)  # need '0' when using r+


def subscriberslist_reseter():  # erases all the entries in the list_subscribers.txt
    with open("list_subscribers.txt", "r+") as subscriberslist:
        subscriberslist.truncate(0)  # need '0' when using r+


def draftlist_verifier(player):  # verifies and adds a new player to the draft list
    with open('list_players.txt', "r+") as draftlist:
        if player in draftlist.read():
            print("name already listed")
            return False
        else:
            draftlist.write(player + "\n")
            return True


# verifies and adds a new subscriber to the list, to prevent the same telegram user_id to subscribe more than one time per week
def subscriberid_verifier(subscriber):
    str_subscriber = str(subscriber)
    with open('list_subscribers.txt', "r+") as subscriberlist:
        if str_subscriber in subscriberlist.read():
            return False
        else:
            subscriberlist.write(str_subscriber + "\n")
            return True


def players_list():
    with open('list_players.txt', "r") as playerlist:
        lines = [line.rstrip() for line in playerlist]
    return lines


def timeframe_verifier_2():  # Sets and verifies if the subscription window is still open
    if 2 <= dayofweek <= 6:  # and datetime.now().hour < 20: # between monday and wednesday
        return True
    else:
        return False


if __name__ == '__main__':
    timeframe_verifier_2()
