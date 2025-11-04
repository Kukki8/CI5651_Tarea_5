from queue import Queue

class Grafo_Bip:
    def __init__(self, conjunto):
        self.pares = [x for x in conjunto if x % 2 == 0]
        self.impares = [x for x in conjunto if x % 2 != 0]

        self.cantidad_par = len(self.pares)
        self.cantidad_impar = len(self.impares)

        self.adyacencias = {p: [] for p in self.pares}

        self.par_con = {p: -1 for p in self.pares}
        self.impar_con = {i: -1 for i in self.impares}
        self.dist = {}

        for p in self.pares:
            for i in self.impares:
                if self.primo(p + i):
                    self.adyacencias[p].append(i)

    def primo(self, n):
        if n <= 1: return False

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True
    
    def bfs(self):
        cola = Queue()

        for p in self.pares:
            if self.par_con[p] == -1:
                self.dist[p] = 0
                cola.put(p)
            else:
                self.dist[p] = float('inf')
        
        self.dist[-1] = float('inf')

        while not cola.empty():
            p = cola.get()
            
            if self.dist[p] < self.dist[-1]:
                for i in self.adyacencias[p]:
                    if self.dist[self.impar_con[i]] == float('inf'):
                        self.dist[self.impar_con[i]] = self.dist[p] + 1
                        cola.put(self.impar_con[i])

        return self.dist[-1] != float('inf')

    def dfs(self, p):
        if p != -1:
            for i in self.adyacencias[p]:
                if self.dist[self.impar_con[i]] == self.dist[p] + 1 and self.dfs(self.impar_con[i]):
                    self.impar_con[i] = p
                    self.par_con[p] = i
                    return True
            
            self.dist[p] = float('inf')
            return False

        return True
    
    def hopcroft_karp(self):

        resultado = 0

        while self.bfs():
            for p in self.pares:
                if self.par_con[p] == -1 and self.dfs(p):
                    resultado += 1

        return resultado

''' Ejemplish
 
conjunto = [1, 2, 3, 4, 6, 8, 9]
grafo = Grafo_Bip(conjunto)

print(grafo.hopcroft_karp())

'''