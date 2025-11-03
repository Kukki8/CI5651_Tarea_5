from collections import deque

class Grafo:
    def __init__(self, agentes, encuentros):
        self.agentes = agentes
        self.encuentros = encuentros
        self.adyacencias = {agente: [] for agente in agentes}
        self.visitados = []

        for a1, a2 in encuentros:
            if a1 in self.adyacencias and a2 in self.adyacencias:
                self.adyacencias[a1].append(a2)
                self.adyacencias[a2].append(a1)

    def dfs_aux(self, agente):
        self.visitados.append(agente)

        for ady in self.adyacencias[agente]:
            if ady not in self.visitados:
                self.dfs_aux(ady)
        
        return len(self.visitados)
    
    def dfs(self, agente):
        self.visitados = []

        return self.dfs_aux(agente)
    
def existe_plan(agentes, encuentros):

    if len(agentes) <= 1:
        return True
    
    grafo = Grafo(agentes, encuentros)

    agente_inicial = list(grafo.adyacencias.keys())[0]
    num_visitados = grafo.dfs(agente_inicial)

    return num_visitados == len(agentes)



''' Ejemplo de grafo conexo

agentes = [ "A", "B", "C", "D", "E"]
encuentros = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E")]

plan = existe_plan(agentes,encuentros)

print(plan)

'''
