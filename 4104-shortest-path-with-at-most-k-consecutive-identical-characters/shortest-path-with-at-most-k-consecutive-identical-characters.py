class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        import heapq

        graph = [[] for _ in xrange(n)]
        for u, v, w in edges:
            graph[u].append((v, w))

        start_count = 1
        pq = [(0, 0, start_count)]
        dist = {}

        while pq:
            cost, u, count = heapq.heappop(pq)

            state = (u, count)
            if state in dist:
                continue
            dist[state] = cost

            if u == n - 1:
                return cost

            for v, w in graph[u]:
                if labels[v] == labels[u]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count <= k and (v, new_count) not in dist:
                    heapq.heappush(pq, (cost + w, v, new_count))

        return -1
        