"""Implementation of the Game"""
import random
import roles


class Game:
    """The Lupus game"""

    def __init__(self):
        self._winner = None
        self._roles = roles.getRolesList()
        self._players = dict()
        self._master = False
        self._rolesGiven = False


    def addPlayer(self, name):
        self._players[name] = "none"


    def getPlayers(self):
        return self._players


    def thereIs(self, name):
        return self._players.get(name) is not None


    def initRoles(self):
        if self._rolesGiven:
            return
        for user in self._players.keys():
            index = random.choice(range(len(self._roles)))
            self._players[user] = self._roles.pop(index)
            self._rolesGiven = True
                # sort the players for the 
        self._players = roles.sort(self._players)


    def gameFull(self):
        return len(self._players.keys()) >= len(self._roles)


    def getRoleOf(self, user):
        return self._players[user]


    def getDescriptionOf(self, role):
        return roles.getDescriptionOf(role)


    def getFactionOf(self, role):
        return roles.getFactionOf(role)


    def getRoleNum(self, role):
        return roles.getNumOf(role)


    def reset(self):
        pass


    def addMaster(self):
        self._master = True


    def isMaster(self):
        return self._master
