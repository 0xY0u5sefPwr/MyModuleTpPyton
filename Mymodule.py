from math import sqrt
def Racines(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        racine1 = (-b - sqrt(delta)) / (2 * a)
        racine2 = (-b + sqrt(delta)) / (2 * a)
        return f"Deux racines réelles : x1 = {racine1}, x2 = {racine2}"
    elif delta == 0:
        racine = -b / (2 * a)
        return f"Une racine double : x = {racine}"
    else:
        return "Pas de racines réelles." 

def trinome(a, b, c):
    Ttuple = []
    delta = b**2 - 4*a*c
    if delta > 0:
        Ttuple.append(2)
        racine1 = (-b - sqrt(delta)) / (2 * a)
        Ttuple.append(racine1)
        racine2 = (-b + sqrt(delta)) / (2 * a)
        Ttuple.append(racine2)
    elif delta == 0:
        Ttuple.append(1)
        racine = -b / (2 * a)
        Ttuple.append(racine)
    else:
        Ttuple.append(0)
    return Ttuple