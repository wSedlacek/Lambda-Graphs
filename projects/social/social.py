from random import randint
from util import Queue


class User:
    def __init__(self, name: str):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id: int, friend_id: int):
        """
        Creates a bi-directional friendship
        """

        if user_id == friend_id:
            raise ValueError("You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            raise ValueError("Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name: str):
        """
        Create a new user with a sequential integer ID
        """

        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
        self.last_id += 1

    def populate_graph(self, num_users: int, avg_friendships: int):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """

        self.last_id = 0
        self.users = {}
        self.friendships = {}

        for i in range(num_users):
            self.add_user(f'{i}')

        for user_id in range(self.last_id):
            friend_request = randint(0, avg_friendships)
            while friend_request > 0:
                random_user = randint(0, num_users - 1)
                if random_user not in self.friendships[user_id] and random_user != user_id:
                    self.add_friendship(user_id, random_user)
                    friend_request -= 1

    def get_friends(self, user_id: int):
        if user_id in self.users:
            return self.friendships[user_id]
        else:
            raise ValueError("This user does not exist...")

    def get_all_social_paths(self, user_id: int):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        queue = Queue()
        queue.push([user_id])
        visited = {user_id}
        connections = {}

        while not queue.empty():
            path = queue.pop()
            user = path[-1]
            connections[user] = path
            for next_user in self.get_friends(user):
                if next_user not in visited:
                    visited.add(next_user)
                    queue.push([*path, next_user])

        return connections

    def avg_friends(self):
        total = 0
        for connection in self.friendships.values():
            total += len(connection)

        return total / len(self.friendships)


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    paths = sg.get_all_social_paths(1)
    print(paths)
