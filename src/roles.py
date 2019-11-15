import json


# Global vars
MASTER = None
ROLES = None


# Extract Vars
with open("db/settings.json") as file:
    data = json.load(file)
    MASTER = data["master"]
    ROLES = data["roles"]


def getRolesList():
    l = list()
    for role, num in ROLES.items():
        for _ in range(num):
            l.append(role)
    return l

def getNumOf(role):
    return ROLES[role]