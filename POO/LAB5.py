class CasNormal:
    def uneMethode(self):
        print("normal")


class CasSpecial:
    def uneMethode(self):
        print("special")


def casQuiConvient(estNormal=True):
    if estNormal :
        a=CasNormal()
        print(a.uneMethode())
    else :
        b=CasSpecial()
        print(b.uneMethode())
uneInstance = casQuiConvient(estNormal=True)
uneInstance.uneMethode() #deja print kayna f l methode i3ni ghi 3ytlha gha texecuti w taffichi

