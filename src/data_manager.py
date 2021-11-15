#!/usr/bin/env python3
import json


class DataManager:
    def __init__(self, settings_path = 'roles.json'):
        # load rolesData
        with open(settings_path) as file:
            self.rolesData = json.load(file)
        # Preprocessing
        self.rolesAvailables = list()
        self.rolesVisibleForSimilars = list()
        for role, info in self.rolesData.items():
            for _ in range(info["num"]):
                self.rolesAvailables.append(role)
            if info['isVisibleForSimilars']:
                self.rolesVisibleForSimilars.append(role)


    def getRolesAvailables(self):
        return self.rolesAvailables


    def getNumOf(self, role):
        return self.rolesData[role]['num']


    def getFactionOf(self, role):
        return self.rolesData[role]["faction"]


    def isVisibleForSimilars(self, role):
        return self.rolesData[role]["isVisibleForSimilars"]


    def getDescriptionOf(self, role):
        return self.rolesData[role]["description"]


    def getImagePathOf(self, role):
        return 'images/' + self.rolesData[role]['image']



# TESTS
if __name__ == "__main__":
    dm = DataManager(settings_path="roles.json")

    role = 'lupo'
    assert dm.getRolesAvailables() == ['lupo', 'lupo']
    assert dm.getNumOf(role) == 2
    assert dm.getFactionOf(role) == 'Cattivo'
    assert dm.isVisibleForSimilars(role)
    assert dm.getDescriptionOf(role) == "Decide con gli altri lupi un qualsiasi personaggio da uccidere"
    assert dm.getImagePathOf(role) == 'default/lupo.jpg'

    print("OK all is correct")