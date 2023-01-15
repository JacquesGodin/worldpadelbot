# worldpadelbot
A simple bot to draft players for the next padel match

Users can interact with three commands:

/help - replies a list of commands the user can use

/enroll - command used to verify if the draft list can still be subscribed and let the user know

/draftlist - returns the players that have been added to the draft list

When a user types a name after using the /enroll command, the user's answer will activate player_enroll function, which will verify if the user has previously subscribed any name into the draft list and, if not, will verify if the name proposed by the user was already in the draft list. In case it isn't it will append the name to list_players.txt file and the telegram user_id to list_subscribers.txt

jobDay and weekly_draft functions set the weekly draft at a specific date and time (given by function t) and post the result to a specific channel. After the draft, all lists will be erased through draftlist_reseter() and subscriberlist_reseter()

Future work:

- Add a control for when there are not enough players to make a game. As of today, it is returning an error as the players.pop function gives an error if it is out of lines
