#!/usr/bin/python3
import json


class DataManager:
    def __init__(self, settings_path = 'roles.json'):
        # load rolesData
        with open(settings_path) as file:
            self.rolesData = json.load(file)


    def _getAllRolesData(self):
        """Return the dictionary with the informations of all the selected roles."""
        roles = dict()
        for role, info in self.rolesData.items():
            roles[role] = {
                'name'         : info['name'],
                'race'         : info['race'],
                'team'         : info['team'],
                'action'       : info['action'],
                'targetStatus' : info['targetStatus'],
                'description'  : info['playerDescription'],
                'image'        : 'images/' + info['image'],
            }
        return roles
    

    def getRolesDataAvailables(self):
        """Return the dictionary with the informations of all the selected roles."""
        roles = dict()
        for role, info in self.rolesData.items():
            if not info['num'] == 0:
                roles[role] = {
                    'name'         : info['name'],
                    'race'         : info['race'],
                    'team'         : info['team'],
                    'action'       : info['action'],
                    'targetStatus' : info['targetStatus'],
                    'description'  : info['playerDescription'],
                    'image'        : 'images/' + info['image'],
                }
        return roles
    

    def getPlayersRoles(self):
        """Return a list with all the rolesName in Game. Roles with num>1 have rapeated names."""
        roles = list()
        for k,v in self.rolesData.items():
            for _ in range(v['num']):
                roles.append(k)
        return roles
    

    def _getAllStatus(self):
        status = list()
        for info in self.rolesData.values():
            statusData = info['targetStatus'] 
            if statusData:
                status.append((statusData[0],statusData[1]))
        return status


    def getStatusAvailables(self, rolesDataAvailables):
        status = list()
        for info in rolesDataAvailables.values():
            r_status = info['targetStatus'] 
            if r_status:
                status.append((r_status[0],r_status[1]))
        return status


    def _getAllOrder(self):
        order = dict()
        for i in range(len(self.rolesData)):
            order[i] = list()
        for id, info in self.rolesData.items():
            order[info['priority']].append(id)
        return order


    def _getAllNightPhases(self):
        """Return a ordered list of phase from the selected roles."""
        phases = list()
        for priority, roles in self._getAllOrder().items():
            if roles != [] and priority != 0:
                for r in roles:
                    phases.append(r)
        return phases


    def getOrderedNightPhases(self, playersRoles):
        """Return a ordered list of phase from the selected roles."""
        phases = list()
        for phase in self._getAllNightPhases():
            if phase in playersRoles:
                phases.append(phase)
        return phases


    def _getAllRules(self):
        """Return all the rules"""
        rules = list()
        for _, info in self.rolesData.items():
            rules.append((info['name'], info['rulesDescription']))
        return rules


    def getRules(self, playersRoles):
        """Return the rules"""
        rules = list()
        for role, info in self.rolesData.items():
            if role in playersRoles:
                rules.append((info['name'], info['rulesDescription']))
        return rules



# TESTS
if __name__ == "__main__":
    dm = DataManager(settings_path="roles.json")

    print('_getAllRolesData')
    print(dm._getAllRolesData())
    print("---")
    print('getRolesDataAvailables')
    print(dm.getRolesDataAvailables())
    print("---")
    print("getPlayersRoles")
    print(dm.getPlayersRoles())
    print("---")
    print("_getAllStatus")
    print(dm._getAllStatus())
    print("---")
    print("getStatusAvailables")
    print(dm.getStatusAvailables(dm.getRolesDataAvailables()))
    print("---")
    print("_getAllOrder")
    print(dm._getAllOrder())
    print("---")
    print("_getAllNightPhases")
    print(dm._getAllNightPhases())
    print("---")
    print("getOrderedNightPhases")
    print(dm.getOrderedNightPhases(dm.getPlayersRoles()))
    print("---")
    print("getRules")
    print(dm.getRules(dm.getPlayersRoles()))
    print("---")

    print("OK all is correct")