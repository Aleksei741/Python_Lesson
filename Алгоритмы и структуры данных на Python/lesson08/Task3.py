# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.


def dfs(graph, start, visited=list()):
    visited.append(start)
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)
    return visited

def graph_generate(n):
    graph = dict()
    for i in range(n):
        graph[i] = list()

    for i in range(n):
        m = int(input(f'Введите кол-во связей {i} вершины: '))
        for j in range(m):
            graph[i].append(int(input('Введите связь: ')))

    return graph

n = int(input('число вершин '))
graph = graph_generate(n)

# graph = {0: [1, 2, 3],
#          1: [0, 2],
#          2: [0, 1, 4],
#          3: [0],
#          4: [2],
#          }

print(graph)
print(f'Порядок обхода {dfs(graph, 0, list())}')