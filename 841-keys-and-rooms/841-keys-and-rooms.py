from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        locked = [True] * len(rooms)
        locked[0] = False
        q = deque()
        q.append(0)
        while len(q):
            node = q.popleft()
            for key in rooms[node]:
                if locked[key]:
                    locked[key] = False
                    q.append(key)
        return not any(locked)