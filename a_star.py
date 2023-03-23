from queue import PriorityQueue
from dists import dists, straight_line_dists_from_bucharest

def h(node):
    return straight_line_dists_from_bucharest.get(node, 0)

def a_star(start, goal='Bucharest'):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        _, current = frontier.get()

        if current == goal:
            break

        for neighbor, cost in dists[current]:
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + h(neighbor)
                frontier.put((priority, neighbor))
                came_from[neighbor] = current

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path

# Exemplo de uso
start = 'Lugoj'
path = a_star(start)
print(path)