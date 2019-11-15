"""Implementation of the Game"""
import random
import roles


class Game:
    """The Lupus game"""

    def __init__(self):
        self._winner = None
        self._roles = roles.getRolesList()
        self._players = list()
    

    def addPlayer(self, name):
        self._players[name] = "none"
    

    def getPlayers(self):
        return self._players
    

    def initRoles(self):
        for user in self._players:
            index = random.choice(range(len(self._roles)))
            self._players[user] = self._roles.pop(index)
    

    def gameFull(self):
        return len(self._players) == len(self._roles)


    def getRoleOf(self, user):
        return self._players[user]


    def getRoleNum(self, role):
        return roles.getNumOf(role)


    def reset(self):
        pass