import json


# Global vars
MASTER = None
ROLES = None
COLORS = {'mago': '#a3d1ff', 'guardia': '#f7ffa3', 'untore': '#a3ffb1', 'lupo': '#ffa3a3'}

with open("db/settings.json") as file:
    data = json.load(file)
    MASTER = data["master"]
    ROLES = data["roles"]


def getRolesList():
    l = list()
    for role, info in ROLES.items():
        for _ in range(info["num"]):
            l.append(role)
    return l


def getNumOf(role):
    return ROLES[role]["num"]


def getDescriptionOf(role):
    return ROLES[role]["description"]


def getFactionOf(role):
    return ROLES[role]["faction"]


def getImageOf(role):
    return ROLES[role]["image"]