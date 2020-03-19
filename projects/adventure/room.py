from typing import List

class Room:
    def __init__(self, name: str, description: str, room_id: int, x: int, y: int):
        self.id = room_id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y

    def __str__(self):
        name = self.name
        description = self.description
        exits = self.get_exits_string()
        return f"""
-------------------
{name}
  {description}
{exits}
"""

    def print_room_description(self, player):
        print(str(self))

    def get_exits(self):
        exits: List[str] = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.w_to is not None:
            exits.append("w")
        if self.e_to is not None:
            exits.append("e")
        return exits

    def get_exits_string(self):
        exits = ', '.join(self.get_exits())
        return f"Exits: [{exits}]"

    def connect_rooms(self, direction, connecting_room):
        if direction == "n":
            self.n_to = connecting_room
            connecting_room.s_to = self
        elif direction == "s":
            self.s_to = connecting_room
            connecting_room.n_to = self
        elif direction == "e":
            self.e_to = connecting_room
            connecting_room.w_to = self
        elif direction == "w":
            self.w_to = connecting_room
            connecting_room.e_to = self
        else:
            print("INVALID ROOM CONNECTION")
            return None

    def get_room_in_direction(self, direction: str):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None


    def connecting_rooms(self):
        rooms: List[Room] = []
        for exit in self.get_exits():
            rooms.append(self.get_room_in_direction(exit))

        return rooms


    def get_coords(self):
        return [self.x, self.y]
