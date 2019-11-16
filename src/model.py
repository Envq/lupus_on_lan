"""Implementation of the Game"""
import random
import data_manager as DM
from collections import OrderedDict


# Global Vars
MASTER = DM.getMaster()
COLORS = DM.getMaster()


class Game:
    """The Lupus game"""

    def __init__(self):
        self._winner = None
        self._roles = DM.getRolesList()
        self._players = OrderedDict()
        self._prePlayers = list()
        self._master = False
        self._rolesGiven = False


    def addPlayer(self, name):
        self._prePlayers.append(name)


    def getPlayers(self):
        return self._players


    def thereIs(self, name):
        for player in self._prePlayers:
            if player.lower() == name.lower():
                return True
        return False


    def initRoles(self):
        if self._rolesGiven:
            return
        for role in self._roles:
            index = random.choice(range(len(self._prePlayers)))
            player = self._prePlayers.pop(index)
            self._players[player] = role
        self._rolesGiven = True


    def getPlayersSimilarTo(self, user):
        target = DM.getRolesVisibleForSimiliars()
        players = list()
        for player, role in self._players.items():
            if role in target and player != user:
                players.append(player)


    def gameFull(self):
        return len(self._prePlayers) == len(self._roles) or self._rolesGiven


    def getRoleOf(self, user):
        return self._players[user]


    def getImageOf(self, role):
        return DM.getImageOf(role)


    def getDescriptionOf(self, role):
        return DM.getDescriptionOf(role)


    def getFactionOf(self, role):
        return DM.getFactionOf(role)


    def getRoleNum(self, role):
        return DM.getNumOf(role)
    

    def getIp(self):
        return DM.getIp()
    

    def getPort(self):
        return DM.getPort()


    def reset(self):
        pass


    def addMaster(self):
        self._master = True


    def isMaster(self):
        return self._master

