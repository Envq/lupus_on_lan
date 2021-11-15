#!/usr/bin/env python3
import random
from data_manager import DataManager


class Game:
    def __init__(self):
        self.state = 'init'
        self.dataManager = DataManager()
        self.winner = None
        self.numPlayers = 0
        self.players = dict()
        self.roles = self.dataManager.getRolesAvailables()
        self.state = 'waitForPlayers'

    
    def isStart(self):
        return self.state == 'start'


    def addPlayer(self, name):
        # check if the state is valid
        if self.state != 'waitForPlayers':
            return False
        # check if the name is valid
        if name == None or name == '' or name.lower() in [p.lower() for p in self.players.keys()]:
            return False
        # add player
        self.players[name] = self.roles[self.numPlayers]
        self.numPlayers += 1
        # check status
        if self.numPlayers == len(self.roles):
            tmp = list(self.players.items())
            random.shuffle(tmp)
            self.players = dict(tmp)
            self.state = 'start'
        return True


    def getPlayersName(self):
        return list(self.players.keys())


    def getPlayersSimilarTo(self, playerName):
        playersSimilar = list()
        playerRole = self.players[playerName]
        if self.dataManager.isVisibleForSimilars(playerRole):
            for p, r in self.players.items():
                if r == playerRole and p != playerName:
                    playersSimilar.append(p)
        return playersSimilar


    def getRoleOf(self, playerName):
        return self.players[playerName]


    def getNumOf(self, role):
        return self.dataManager.getNumOf(role)


    def getFactionOf(self, role):
        return self.dataManager.getFactionOf(role)


    def getDescriptionOf(self, role):
        return self.dataManager.getDescriptionOf(role)


    def getImagePathOf(self, role):
        return self.dataManager.getImagePathOf(role)



# TESTS
if __name__ == "__main__":
    g = Game()

    # WAIT FOR PLAYERS
    assert not g.isStart()
    assert g.state == 'waitForPlayers'
    assert g.roles == ['lupo', 'lupo']
    assert g.players == {}

    res = g.addPlayer('a')
    assert res
    assert g.state == 'waitForPlayers'
    assert g.players == {'a':'lupo'}

    res = g.addPlayer('a')
    assert not res
    assert g.state == 'waitForPlayers'
    assert g.players == {'a':'lupo'}

    res = g.addPlayer('b')
    assert res
    assert g.state == 'start'
    assert g.players == {'a':'lupo', 'b':'lupo'}
    assert g.isStart()

    res = g.addPlayer('b')
    assert not res
    assert g.state == 'start'
    assert g.players == {'a':'lupo', 'b':'lupo'}

    # METHODS
    assert g.getPlayersName() == ['a', 'b'] or g.getPlayersName() == ['b', 'a']
    assert g.getPlayersSimilarTo('a') == ['b']
    assert g.getPlayersSimilarTo('b') == ['a']
    assert g.getRoleOf('a') == 'lupo'

    print("OK all is correct")
