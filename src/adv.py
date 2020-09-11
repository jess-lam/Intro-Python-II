from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

#
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

new_player = Player("Jess", room["outside"])

#print(f" {new_player.name} is in {new_player.current_room.name}")
#print(new_player.current_room.description)

#$print(room[new_player.current_room].description)


#print(new_player)
# print(room.items())
# print(room.get("outside"))
# print(room.get("outside").name)
# print(room.get("outside").description)

# Write a loop that:
"""
for r in room:
    print(room[r].name)
    print(room[r].description)
"""

#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#while True:
#print(f"\n Currently in room: {new_player.current_room.name}")
#print(f"\n Room Description: {new_player.current_room.description}")
#print(new_player.current_room)

#new_place = new_player.current_room.n_to
#print(new_place)


while True:
    selection = input("Please make a move.")
    if selection == 'n' or selection == 's' or selection == 'e' or selection == 'w':
        if selection == 'n':
            return new_player.current_room.n_to
            print(new_player.current_room.n_to)
        elif selection == 's':
            return new_player.current_room.s_to
            print(new_player.current_room.s_to)
        elif selection == 'e':
            return new_player.current_room.e_to
            print(new_player.current_room.e_to)
        elif selection == 'w':
            return new_player.current_room.w_to
            print(new_player.current_room.w_to)
    elif selection == 'q':
        print(f"See you next time {new_player.name}!")
    else:
        print("Movement isn't allowed. Please select n for North, s for South, e for East, w for West, or q for Quit.")
        



#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

