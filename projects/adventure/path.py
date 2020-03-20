from random import shuffle
from typing import Dict, List, Set, Tuple
from util import Queue, Stack, inverse_direction

from room import Room


class Path:
    def __init__(self):
        self.rooms: Dict[int, Set[Room]] = {}

    def add_room(self, room: Room):
        self.rooms[room.id] = set()

    def add_edge(self, room_1: Room, room_2: Room):
        if room_1:
            if room_1.id not in self.rooms:
                self.add_room(room_1)

            self.rooms[room_1.id].add(room_2)

        if room_2:
            if room_2.id not in self.rooms:
                self.add_room(room_2)

            self.rooms[room_2.id].add(room_1)

    def full_path(self, starting_room: Room):
        stack = Stack()
        path: List[str] = []

        # Add First Item to Stack
        stack.push([starting_room, None])
        visited = {starting_room}

        # While stack is not empty
        while not stack.empty():

            # Take first Item off the stack
            items = stack.pop()
            room: Room = items[0]

            new_room = False

            # Pick a direction that is not visited.
            exits = room.get_exits()
            shuffle(exits)
            for exit in exits:
                potential_room: Room = room.get_room_in_direction(exit)

                if potential_room not in visited:
                    # Move in that direction and append it
                    path.append(exit)
                    visited.add(potential_room)

                    # Put that on the stack
                    stack.push(items)
                    stack.push([potential_room, inverse_direction(exit)])
                    new_room = True
                    break

            if len(visited) == len(self.rooms):
                return path

            # If there are no potential rooms then backtrack
            backtrack: str = items[1]
            if not new_room and backtrack:
                path.append(backtrack)
