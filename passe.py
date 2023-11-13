def NbCMin(passe):
    N = 0
    for i in range(len(passe)):
        if ord("a") <= ord(passe[i]) <= ord("z"):
            N = N + 1
    return N
def NbCMaj(passe):
    A = 0
    for i in range(len(passe)):
        if ord("A") <= ord(passe[i]) <= ord("Z"):
            A += 1
    return A
def NbCAlpha(passe):
    B = 0
    for i in range(len(passe)):
        if ord("A") <= ord(passe[i]) <= ord("Z") or ord("a") <= ord(passe[i]) <= ord("z"):
            g = 0
        else:
             B+= 1
    return B
def LongMaj(passe):
    C = 0
    D = 0
    for i in range(len(passe)):
        if ord("A") <= ord(passe[i]) <= ord("Z"):
            C += 1
        else:
            C = 0
        if D < C:
            D = C
    return D
def LongMin(passe):
    D = 0
    E = 0
    for i in range(len(passe)):
        if ord("a") <= ord(passe[i]) <= ord("z"):
            D += 1
        else:
            D = 0
        if E < D:
            E = D
    return E
def score(passe):
    S = len(passe) * 4 + (len(passe) - NbCMin(passe)) * 3 + (len(passe) - NbCMaj(passe)) * 2 + NbCAlpha(passe) * 5 - LongMin(passe) * 2 - LongMaj(passe) * 2
    return S
passe = input("Type password: ")
S = score(passe)
if S < 20:
    print("Very Weak")
elif 20 <= S < 40:
    print("Weak")
elif 40 <= S < 80:
    print("Strong")
else:
    print("Very Strong")