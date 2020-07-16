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
rooms_seen = []
# push the first room
rooms_seen.append(player.current_room.id)

# while the dictionary is less than len(graph)
for i in range(5):
    # discover what the new id is
    current_room = player.current_room.id
                                    # fill in direction connection for both the previous and current room
    if player.current_room.id not in visited:
        visited[player.current_room.id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
    
    # get the possible exit directions of current room
    directions = player.current_room.get_exits()
    compass = {'n':'s', 's':'n', 'w':'e', 'e':'w'}

    x = 0
    # if that direction is empty/null/"?"
    print(directions)
    
    if visited[player.current_room.id][directions[x]] == '?':
        print('hello')
        if player.travel(directions[x]) is not None:
            next_room = player.current_room.get_room_in_direction(directions[x])
    

            visited[player.current_room.id][directions[x]] = next_room
            print('hello')

            if next_room not in visited:
                visited[player.current_room.id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
            visited[next_room][compass[directions[x]]] = player.current_room.id

            print(visited)
            

            
            # player.travel(directions[x])



            

        # move to that room (reassign current_room)
    # elif try the next direction in the exit list
    # if all possible exit directions are filled in, 
        # pop the previous direction off the top of the list/stack 
    

        ## this will leave you stuck at the end of a line
        ## will need to traverse/travel back down a stack until you find a 
# build a stack of the directions you've gone



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
