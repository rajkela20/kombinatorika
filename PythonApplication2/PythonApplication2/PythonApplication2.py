from collections import deque

def bfs(graph, residual, source, sink, parent):
    """Поиск в ширину для нахождения дополняющего пути."""
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        current = queue.popleft()
        for neighbor, capacity in graph[current].items():
            # Если сосед не посещен и есть остаточная пропускная способность
            if neighbor not in visited and residual[current][neighbor] > 0:
                parent[neighbor] = current
                if neighbor == sink:
                    return True
                queue.append(neighbor)
                visited.add(neighbor)
    return False

def edmonds_karp(graph, source, sink):
    """Алгоритм Эдмондса-Карпа для нахождения максимального потока."""
    # Инициализация остаточной сети
    residual = {u: {v: capacity for v, capacity in edges.items()} for u, edges in graph.items()}
    max_flow = 0
    parent = {}

    while bfs(graph, residual, source, sink, parent):
        # Находим минимальную пропускную способность в найденном пути
        path_flow = float('Inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u

        # Обновляем остаточную сеть
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][a] += path_flow
            v = u

        max_flow += path_flow

    return max_flow

# Пример графа
graph = {
    's': {'a': 10, 'b': 5},
    'a': {'b': 15, 't': 10},
    'b': {'t': 10},
    't': {}
}

source = 's'
sink = 't'

max_flow = edmonds_karp(graph, source, sink)
print(f"Максимальный поток: {max_flow}")
