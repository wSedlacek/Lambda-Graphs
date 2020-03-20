from typing import List
from ast import literal_eval

from room import Room
from player import Player
from world import World
from path import Path

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
world.print_rooms()


def test(traversal_path: List[str]):
    player = Player(world.starting_room)

    visited_rooms = set()
    player.current_room = world.starting_room
    visited_rooms.add(player.current_room)

    for move in traversal_path:
        player.travel(move)
        visited_rooms.add(player.current_room)

    if len(visited_rooms) == len(room_graph):
        print(
            f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
    else:
        print("TESTS FAILED: INCOMPLETE TRAVERSAL")
        print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


def repl():
    player = Player(world.starting_room)

    player.current_room.print_room_description(player)
    while True:
        cmds = input("-> ").lower().split(" ")
        if cmds[0] in ["n", "s", "e", "w"]:
            player.travel(cmds[0], True)
        elif cmds[0] == "q":
            break
        else:
            print("I did not understand that command.")


path = Path()

for room in world.rooms.values():
    for next_room in room.connecting_rooms():
        path.add_edge(room, next_room)

pathing = None
while not pathing or len(pathing) >= 960:
    pathing = path.full_path(world.starting_room)
    if len(pathing) < 975:
        print(len(pathing))

test(pathing)
