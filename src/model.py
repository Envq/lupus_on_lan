#!/usr/bin/python3
import random

from data_manager import DataManager


class Game:
    # DEPRECED
    def __init__(self):
        self.dataManager  = DataManager()
        self.rolesData    = self.dataManager.getRolesAvailables()
        self.rolesList    = self.dataManager.getPlayersRoles()
        self.nightPhases  = self.dataManager.getNightPhases(self.rolesList)
        self.players      = dict()
        self.master       = None
        self._userCounter = 0 
        self._addFake()
    

    def _addFake(self):
        # ROLES_LIST
        self.rolesList = ['werewolf', 'villager', 'seer']
        # PLAYERS
        self.players = dict()
        self.players['192.168.1.10'] = {
            'name' : 'Gino',
            'role' : 'werewolf',
            'death': False,
        }
        self.players['192.168.1.11'] = {
            'name' : 'Ezio',
            'role' : 'villager',
            'death': False,
        }
        self.players['192.168.1.12'] = {
            'name' : 'Giuggiola',
            'role' : 'villager',
            'death': False,
        }
        self.players['192.168.1.12'] = {
            'name' : 'Sdrumello',
            'role' : 'seer',
            'death': True,
        }
        # ROLES
        self.rolesData = dict()
        self.rolesData['werewolf'] = {
            'name' : 'Lupo Mannaro',
            'race' : 'Mostro',
            'team' : 'Mostro',
        }
        self.rolesData['villager'] = {
            'name' : 'Contadino',
            'race' : 'Umano',
            'team' : 'Umano',
        }
        self.rolesData['seer'] = {
            'name' : 'Veggente',
            'race' : 'Umano',
            'team' : 'Umano',
        }
        # NIGHTPHASES
        self.nightPhases =  [('seer',False), ('werewolf',True)]


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
        return len(self.getUsersId()) == len(self.rolesList)+1


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
            if len(self.players) == len(self.rolesList):
                return False
            self.players[id] = {
                'name'     : name,
                'role'     : self.rolesList[self._userCounter],
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
        return f'{100 * len(self.getUsersId()) // (len(self.rolesList)+1)}%'

    
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
        return self.players


    def getRolesData(self):
        return self.rolesData

    
    def getNightPhases(self):
        return self.nightPhases


    def processNightData(self, data):
        print(data)     



# TESTS
if __name__ == "__main__":
    g = Game()

    print(g.players)
    print(g.getNightPhases())


    print("OK all is correct")
