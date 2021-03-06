def camino(s, t, c, f): # construcción de un camino aumentante
    cola = [s]
    usados = set()
    camino = dict()
    while len(cola) > 0:
        u = cola.pop(0)
        usados.add(u)
        for (w, v) in c:
            if w == u and v not in cola and v not in usados:
                actual = f.get((u, v), 0)
                dif = c[(u, v)] - actual
                if dif > 0:
                    cola.append(v)
                    camino[v] = (u, dif)
    if t in usados:
        return camino
    else: # no se alcanzó
        return None
 
def ford_fulkerson(c, s, t): # algoritmo de Ford y Fulkerson
    if s == t:
        return 0
    maximo = 0
    f = dict()
    while True:
        aum = camino(s, t, c, f)
        if aum is None:
            break # ya no hay
        incr = min(aum.values(), key = (lambda k: k[1]))[1]
        u = t
        while u in aum:
            v = aum[u][0]
            actual = f.get((v, u), 0) # cero si no hay
            inverso = f.get((u, v), 0)
            f[(v, u)] = actual + incr
            f[(u, v)] = inverso - incr
            u = v
        maximo += incr
    return maximo
 
# datos tomados de:
# http://www.aduni.org/courses/algorithms/courseware/handouts/Reciation_09.html
c = {(0, 1): 16, (0, 2): 13, (1, 2): 10, (2, 1): 4, (3, 2): 9, \
(1, 3): 12, (2, 4): 14, (4, 3): 7, (3, 5): 20, (4, 5): 4}
s = 0
t = 5
print(ford_fulkerson(c, s, t))
