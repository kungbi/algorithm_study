import sys


def input():
    return sys.stdin.readline().rstrip()


class Player:
    def __init__(self, level, name):
        self.level = level
        self.name = name


class Room:
    def __init__(self, level, maxPlayers):
        self.level = level
        self.players = []
        self.maxPlayers = maxPlayers

    def add(self, level, name):
        self.players.append(Player(level, name))

    def isFull(self):
        return len(self.players) == self.maxPlayers

    def isAvailable(self, level):
        return self.level - 10 <= level <= self.level + 10

    def __str__(self):
        self.players.sort(key=lambda x: x.name)
        tmp = ""
        for player in self.players:
            tmp += f"{player.level} {player.name}\n"
        return tmp


def main():
    global maxPlayer
    p, m = map(int, input().split())

    rooms = []
    for _ in range(p):
        level, name = input().split()
        level = int(level)

        finalRoom = None
        for room in rooms:
            if not room.isAvailable(level):
                continue
            if room.isFull():
                continue
            finalRoom = room
            break

        if finalRoom == None:
            finalRoom = Room(level, m)
            rooms.append(finalRoom)

        finalRoom.add(level, name)

    for room in rooms:
        print("Started!" if room.isFull() else "Waiting!")
        print(room, end="")


main()
