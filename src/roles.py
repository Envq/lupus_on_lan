MASTER_NAME = "master"

roles = {
    "contadino" : 1,
    "lupo"      : 1,
    "veggente"  : 0,
    "mago"      : 0,
    "guardia"   : 0,
    "untore"    : 0,
    "massone"   : 0,
    "criceto"   : 0,
}


def getRolesList():
    l = list()
    for role, num in roles.items():
        for _ in range(num):
            l.append(role)
    return l

def getNumOf(role):
    return roles[role]
