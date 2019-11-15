roles = {
    "contadino" : 2,
    "lupo"      : 1,   
    "veggente"  : 1, 
    "mago"      : 1, 
    "guardia"   : 1, 
    "untore"    : 1,  
    "massone"   : 1,  
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