#!/usr/bin/python3
import random

from data_manager import DataManager


class Game:
    # DEPRECED
    def __init__(self):
        self.dataManager  = DataManager()
        self.rolesData    = self.dataManager.getRolesDataAvailables()
        self.statusData   = self.dataManager.getStatusAvailables(self.rolesData)
        self.playersRoles = self.dataManager.getPlayersRoles()
        self.nightPhases  = self.dataManager.getOrderedNightPhases(self.playersRoles)
        self.players      = dict()
        self.master       = None
        self._userCounter = 0 
        self._addFake()
    

    def _addFake(self):
        # ROLES_LIST
        self.playersRoles = ['werewolf'] * 16
        # PLAYERS
        self.players = dict()
        self.players['192.168.1.1']  = {'name' : 'A', 'role' : 'werewolf',      'race' : 'Mostro'}
        self.players['192.168.1.2']  = {'name' : 'B', 'role' : 'seer',          'race' : 'Umano'}
        self.players['192.168.1.3']  = {'name' : 'C', 'role' : 'villager',      'race' : 'Umano'}
        self.players['192.168.1.4']  = {'name' : 'D', 'role' : 'medium',        'race' : 'Umano'}
        self.players['192.168.1.5']  = {'name' : 'E', 'role' : 'possessed',     'race' : 'Umano'}
        self.players['192.168.1.6']  = {'name' : 'F', 'role' : 'bodyguard',     'race' : 'Umano'}
        self.players['192.168.1.7']  = {'name' : 'G', 'role' : 'owlman',        'race' : 'Umano'}
        self.players['192.168.1.8']  = {'name' : 'H', 'role' : 'freemasons',    'race' : 'Umano'}
        self.players['192.168.1.9']  = {'name' : 'I', 'role' : 'werehamster',   'race' : 'Umano'}
        self.players['192.168.1.10'] = {'name' : 'J', 'role' : 'mythomaniac',   'race' : 'Umano'}
        self.players['192.168.1.11'] = {'name' : 'K', 'role' : 'mage',          'race' : 'Umano'}
        self.players['192.168.1.12'] = {'name' : 'L', 'role' : 'infector',      'race' : 'Mostro'}
        self.players['192.168.1.13'] = {'name' : 'M', 'role' : 'villager',      'race' : 'Umano'}
        self.players['192.168.1.14'] = {'name' : 'N', 'role' : 'werewolf',      'race' : 'Mostro'}
        self.players['192.168.1.15'] = {'name' : 'O', 'role' : 'werewolf',      'race' : 'Mostro'}
        self.players['192.168.1.16'] = {'name' : 'P', 'role' : 'werewolf',      'race' : 'Mostro'}
        # ROLES
        self.rolesData = self.dataManager._getAllRolesData()
        # STATUS
        self.statusData = self.dataManager._getAllStatus()
        # NIGHTPHASES
        self.nightPhases = self.dataManager._getAllNightPhases()


    def _newGame(self):
        tmp = list(self.players.items())
        random.shuffle(tmp)
        self.players = dict(tmp)


    def getUsersId(self):
        """Returns the list of players + master"""
        playersId = list(self.players.keys())
        if self.master:
            return playersId + [self.master]
        return playersId


    def isAlreadyLogged(self, id):
        """Returns True if the user is already present"""
        return id in self.getUsersId()


    def lobbyIsFull(self):
        """Returns True if the lobby is full"""
        return len(self.getUsersId()) == len(self.playersRoles)+1


    def addUser(self, id, name):
        """Returns True if the addition of the user was successful"""
        # check if the user is alredy register
        if id in self.getUsersId():
            return False
        # check if the name is valid
        if name == None or name == '' or name.lower() in [p['name'].lower() for p in self.players.values()]:
            return False

        # add user
        if name.lower() == 'master':
            if self.master:
                return False
            self.master = id
        else:
            if len(self.players) == len(self.playersRoles):
                return False
            self.players[id] = {
                'name'     : name,
                'role'     : self.playersRoles[self._userCounter],
                'death'    : False,
            }
            self._userCounter += 1
            
        # Check if the game can start
        if self.lobbyIsFull():
            self._newGame()
        return True


    def getUsersNames(self):
        playersName = [v['name'] for v in self.players.values()]
        if self.master:
            return ['master'] + playersName
        return playersName
    

    def getProgressLobbyStr(self):
        return f'{100 * len(self.getUsersId()) // (len(self.playersRoles)+1)}%'

    
    def isMaster(self, id):
        return id != None and self.master == id
    

    def getNameOf(self, id):
        return self.players[id]['name']


    def getRoleDataOf(self, id):
        playerRole = self.players[id]['role']
        return self.rolesData[playerRole]


    def getPlayersSimilarTo(self, id):
        playersSimilar = list()
        playerRole = self.players[id]['role']
        for p, info in self.players.items():
            if info['role'] == playerRole and p != id:
                playersSimilar.append(p)
        return playersSimilar


    def getPlayers(self):
        return sorted(self.players.values(), key=lambda x: x['role'])
    

    def getPlayersNames(self):
        return [p['name'] for p in self.players.values()]


    def getRolesData(self):
        return self.rolesData

    
    def getNightPhases(self):
        return self.nightPhases


    def getStatusData(self):
        return self.statusData


    def processNightData(self, data):
        print(data)     




# TESTS
if __name__ == "__main__":
    g = Game()

    for p in g.getPlayersNames():
        print(p)


    print("OK all is correct")
