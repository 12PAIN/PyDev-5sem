from Structures.Graph import Graph


def deixtra(graph, start, end):
    distances = {vid: float('inf') if vid != start else 0 for vid in graph.getVertices()}
    previous_vertices = {vid: None for vid in graph.getVertices()}
    visited = set()

    while distances:
        current = graph.getVertex(min(distances, key=distances.get))
        cid = current.getId()
        visited.add(cid)

        if cid == end:
            break

        neighbors = current.getConnections()
        for neighbor in neighbors:
            nid = neighbor.getId()
            if neighbor not in visited:
                weight = current.getWeight(neighbor)
                distance = distances[cid] + weight
                try:
                    if distance < distances[nid]:
                        distances[nid] = distance
                        previous_vertices[nid] = current
                except KeyError:
                    raise KeyError('Пути нет')

        del distances[cid]

    if previous_vertices[end]:
        path = []
        current = graph.getVertex(end)
        while current:
            path.insert(0, current.getId())
            current = previous_vertices[current.getId()]
        return path, distances[end]
    else:
        return None, None


def getCities(graph):
    start = input()
    end = input()
    if start not in graph or end not in graph:
        raise ValueError('Город введён неверно!')
    return start, end


g = Graph()

g.addEdge('Белово', 'Ленинск-Кузнецкий', 31)
g.addEdge('Ленинск-Кузнецкий', 'Киселевск', 79)
g.addEdge('Белово', 'Киселевск', 51)
g.addEdge('Белово', 'Гурьевск', 28)
g.addEdge('Гурьевск', 'Киселевск', 102)
g.addEdge('Ленинск-Кузнецкий', 'Мыски', 150)
g.addEdge('Киселевск', 'Кемерово', 154)
g.addEdge('Кемерово', 'Новосибирск', 204)
g.addEdge('Мыски', 'Новосибирск', 348)


def main():
    start, end = getCities(g)
    try:
        path, distance = deixtra(g, start, end)
        if path is None and distance is None:
            print('Пути между городами нет')
            return
        print(f'{path},{distance}')
    except KeyError:
        print('Пути между городами нет')

# main()
