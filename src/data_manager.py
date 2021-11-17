#!/usr/bin/env python3
import json


class DataManager:
    def __init__(self, settings_path = 'roles.json'):
        # load rolesData
        with open(settings_path) as file:
            self.rolesData = json.load(file)
        # Preprocessing
        self.rolesAvailables = list()
        self.descriptions = dict()
        for role, info in self.rolesData.items():
            for _ in range(info["num"]):
                self.rolesAvailables.append(role)
            if info["num"] > 0:
                self.descriptions[info['name']] = info['description']


    def getRolesAvailables(self):
        return self.rolesAvailables


    def getDescriptions(self):
        return self.descriptions


    def getNumOf(self, role):
        return self.rolesData[role]['num']


    def getNameOf(self, role):
        return self.rolesData[role]['name']


    def getFactionOf(self, role):
        return self.rolesData[role]["faction"]


    def getSeenAs(self, role):
        return self.rolesData[role]["seenAs"]


    def getIsVisibleForSimilars(self, role):
        return self.rolesData[role]["isVisibleForSimilars"]


    def getDescriptionOf(self, role):
        return self.rolesData[role]["description"]


    def getPlayerDescriptionOf(self, role):
        return self.rolesData[role]["playerDescription"]


    def getImagePathOf(self, role):
        return 'images/' + self.rolesData[role]['image']



# TESTS
if __name__ == "__main__":
    dm = DataManager(settings_path="roles.json")

    role = 'werewolf'
    assert dm.getRolesAvailables() == ['werewolf', 'werewolf']
    assert dm.getDescriptions() == {'Lupo Mannaro': "Ad inizio partita i lupi mannari si riconoscono. Ogni notte si accordano per sbranare uno degli abitanti del villaggio che, salvo interventi di personaggi speciali, verrà dichiarato morto dal master all'inizio della giornata successiva."}
    assert dm.getNumOf(role) == 2
    assert dm.getNameOf(role) == 'Lupo Mannaro'
    assert dm.getFactionOf(role) == 'Cattivo'
    assert dm.getSeenAs(role) == 'Cattivo'
    assert dm.getIsVisibleForSimilars(role)
    assert dm.getDescriptionOf(role) == "Ad inizio partita i lupi mannari si riconoscono. Ogni notte si accordano per sbranare uno degli abitanti del villaggio che, salvo interventi di personaggi speciali, verrà dichiarato morto dal master all'inizio della giornata successiva."
    assert dm.getPlayerDescriptionOf(role) == "Decide con gli altri lupi un qualsiasi personaggio da uccidere."
    assert dm.getImagePathOf(role) == 'images/default/lupo.jpg'
    
    print("OK all is correct")