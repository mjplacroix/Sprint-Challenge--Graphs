from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk

# start with a dictionary to store traversed rooms with directions possible
visited = {}
# start with a list/stack to store the current room id
path = []
# # push the first room
# rooms_seen.append(player.current_room.id)

# while the dictionary is less than len(graph)
for i in range(10):
    # discover what the new id is
    current_room = player.current_room.id
                                    # fill in direction connection for both the previous and current room
    if player.current_room.id not in visited:
        visited[player.current_room.id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
    
    # get the possible exit directions of current room
    directions = player.current_room.get_exits()
    compass = {'n':'s', 's':'n', 'w':'e', 'e':'w'}

    x = 0
    print(f'>{player.current_room.id, player.current_room.get_exits()}')

    # I need to be able to iterate through a <for?> loop of options - exits list
    x = 0
    for direction in directions:
        # if I find an unfilled available direction
        # if that direction is empty/null/"?"
        if visited[player.current_room.id][direction] == '?':

            # go that direction
            # get the room number of the next room    
            next_room = player.current_room.get_room_in_direction(directions[x]).id
            # fill in the directional table of the current room
            visited[player.current_room.id][directions[x]] = next_room

            # store the room number of the current room as previous room
            previous_room = player.current_room.id
            # add direction to path stack
            path.append(directions[x])
            # move to the next room
            player.travel(directions[x])

            # if next room (now current room) doesn't exist, create a table entry
            if player.current_room.id not in visited:
                visited[player.current_room.id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}

            # fill in the directional table of the current room with the previous room
            visited[player.current_room.id][compass[directions[x]]] = previous_room
        else:
            x += 1

            # if all possible exit directions have been tried 


        # if I don't find an unfilled available direction, 
        # pop the previously traveled direction off the path stack and travel the opposite direction via the compass dictionary
        # break out of the loop and go that way
        if x == len(directions):
            # pop the previous direction off the top of the list/stack 
            backtrack = path.pop()
            # look up opposite direction in compass and traverse
            player.travel(compass[backtrack])
            print(f'ROOM: {player.current_room.id}')
        

        


        





""" below is deprecated code I believe """

    # # if that direction is empty/null/"?"
    # if visited[player.current_room.id][directions[x]] == '?':
    #     # if a room in that direction exists
    #     if player.current_room.get_room_in_direction(directions[x]):    ## <- unneccesary if only trying possible exits

    #         # # add the current room number to the stack
    #         # rooms_seen.append(player.current_room.id)

    #         # get the room number of the next room    
    #         next_room = player.current_room.get_room_in_direction(directions[x]).id
    #         # fill in the directional table of the current room
    #         visited[player.current_room.id][directions[x]] = next_room

    #         # store the room number of the current room as previous room
    #         previous_room = player.current_room.id
    #         # add direction to path stack
    #         path.append(directions[x])
    #         # move to the next room
    #         player.travel(directions[x])

    #         # if next room (now current room) doesn't exist, create a table entry
    #         if player.current_room.id not in visited:
    #             visited[player.current_room.id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}

    #         # fill in the directional table of the current room with the previous room
    #         visited[player.current_room.id][compass[directions[x]]] = previous_room
    # else:
    #     # else increment the counter to try the next direction in the exit list
    #     x += 1   
    #     print(x, len(directions), path, visited)   

    # # if all possible exit directions have been tried 
    # if x == len(directions):
    #     # pop the previous direction off the top of the list/stack 
    #     backtrack = path.pop()
    #     # look up opposite direction in compass and traverse
    #     player.travel(compass[backtrack])
    #     print(f'ROOM: {player.current_room.id}')




# traversal_path = ['n', 'n']
traversal_path = []


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)
    print(f"Room: {player.current_room.id} -- Exits: {player.current_room.get_exits()}")

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
