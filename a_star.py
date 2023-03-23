from dists import dists, straight_line_dists_from_bucharest

def heuristic(node):
    return straight_line_dists_from_bucharest[node]

# goal sempre sera 'bucharest'
def a_star(start, goal='Bucharest'):
    # Nó = Estado inicial do problema
    node = start
    # Custo-Caminho = 0
    path_cost = 0
    # Borda = CRIAR-FILA-PRIORIDADES()
    frontier = []
    # INSERIR-PRIORIDADES(Borda, Nó)
    frontier.append((path_cost + heuristic(node), node))
    # Explorado = Æ
    explored = set()
    
    # REPITA
    while frontier:
        # SE VAZIA(Borda) ENTÃO RETORNAR Falha
        if not frontier:
            return "Falha"
        
        # Nó = REMOVER-PRIORIDADES(Borda)
        (priority, node) = frontier.pop(0)
        
        # SE Nó é Objetivo ENTÃO RETORNAR Solução
        if node == goal:
            return path_cost
        
        # Explorado = Explorado È {Nó}
        explored.add(node)
        
        # AçõesPossíveis = Ações possíveis a partir de Nó
        possible_actions = dists[node]
        
        # PARA CADA Ação Î AçõesPossíveis FAÇA
        for action in possible_actions:
            # Filho = NÓ-FILHO(Nó, Ação)
            child_node, cost = action
            child_cost = path_cost + cost
            
            # SE Filho não está na Borda E Filho Ï Explorado ENTÃO INSERIR-PRIORIDADES(Borda, Filho)
            if (child_node not in [x[1] for x in frontier]) and (child_node not in explored):
                frontier.append((child_cost + heuristic(child_node), child_node))
            
            # SENÃO
            else:
                # SE Filho Está na Borda E g(n)+h(n) na Borda é maior ENTÃO
                for i, (priority, frontier_node) in enumerate(frontier):
                    if frontier_node == child_node and child_cost < path_cost:
                        # Substitui o nó na Borda por Filho
                        del frontier[i]
                        frontier.append((child_cost + heuristic(child_node), child_node))
                        break
        
        # FIM PARA
    # FIM REPITA

