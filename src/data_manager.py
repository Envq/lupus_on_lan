#!/usr/bin/python3
import json


class DataManager:
    def __init__(self, settings_path = 'roles.json'):
        # load rolesData
        with open(settings_path) as file:
            self.rolesData = json.load(file)
        

    def getRolesAvailables(self):
        """Return the dictionary with the informations of all the selected roles."""
        roles = dict()
        for role, info in self.rolesData.items():
            if not info['num'] == 0:
                roles[role] = {
                    'name'        : info['name'],
                    'race'        : info['race'],
                    'team'        : info['team'],
                    'description' : info['playerDescription'],
                    'image'       : 'images/' + info['image'],
                }
        return roles
    

    def getPlayersRoles(self):
        """Return a list with all the rolesName in Game. Roles with num>1 have rapeated names."""
        roles = list()
        for k,v in self.rolesData.items():
            for _ in range(v['num']):
                roles.append(k)
        return roles
    

    def _getRolesOrder(self):
        order = dict()
        for i in range(len(self.rolesData)):
            order[i] = list()
        for id, info in self.rolesData.items():
            order[info['priority']].append(id)
        return order


    def getNightPhases(self, roles_availables):
        """Return a ordered list of phase from the selected roles."""
        phases = list()
        for priority, roles in self._getRolesOrder().items():
            if roles != [] and priority != 0:
                for r in roles:
                    if r in roles_availables:
                        phases.append((r, True))
        return phases

# TESTS
if __name__ == "__main__":
    dm = DataManager(settings_path="roles.json")

    print('getRolesAvailables')
    print(dm.getRolesAvailables())
    print("---")
    print("getPlayersRoles")
    print(dm.getPlayersRoles())
    print("---")
    print("_getRolesOrder")
    print(dm._getRolesOrder())
    print("---")
    print("getNightPhases")
    print(dm.getNightPhases(dm.getPlayersRoles()))
    print("---")

    print("OK all is correct")