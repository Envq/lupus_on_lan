import json

# Vars
with open("db/settings.json") as file:
    data = json.load(file)
    MASTER = data["master"]
    ROLES = data["roles"]
    COLORS = data["colors"]
    VISIBLE = data["visible"]


def getRolesList():
    l = list()
    for role, info in ROLES.items():
        for _ in range(info["num"]):
            l.append(role)
    return l


def getRolesVisible():
    return VISIBLE


def getNumOf(role):
    return ROLES[role]["num"]


def getDescriptionOf(role):
    return ROLES[role]["description"]


def getFactionOf(role):
    return ROLES[role]["faction"]


def getImageOf(role):
    return ROLES[role]["image"]
