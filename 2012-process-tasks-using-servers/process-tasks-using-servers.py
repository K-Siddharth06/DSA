import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        available = []
        busy = []
        ans = []

        for i in range(len(servers)):
            heapq.heappush(available, (servers[i], i))

        time = 0

        for i in range(len(tasks)):
            time = max(time, i)

            while busy and busy[0][0] <= time:
                end, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    end, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            weight, idx = heapq.heappop(available)
            ans.append(idx)

            heapq.heappush(busy, (time + tasks[i], weight, idx))

        return ans