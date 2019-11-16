import json

# Vars
with open("db/settings.json") as file:
    data = json.load(file)
    MASTER = data["master"]
    IP = data["ip"]
    PORT = data["port"]
    ROLES = data["roles"]
    COLORS = data["colors"]
    ROLES_VISIBLE_FOR_SIMILARS = [
        role for role, info in ROLES.items() if info["visibleForSimilars"]]


def getRolesList():
    l = list()
    for role, info in ROLES.items():
        for _ in range(info["num"]):
            l.append(role)
    return l


def getIp():
    # Default is "localhost"
    return IP


def getPort():
    # Default is 5000
    return PORT


def getMaster():
    return MASTER


def getColors():
    return COLORS


def getRolesVisibleForSimiliars():
    return ROLES_VISIBLE_FOR_SIMILARS


def getNumOf(role):
    return ROLES[role]["num"]


def getDescriptionOf(role):
    return ROLES[role]["description"]


def getFactionOf(role):
    return ROLES[role]["faction"]


def getImageOf(role):
    return ROLES[role]["image"]