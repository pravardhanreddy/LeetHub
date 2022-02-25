import numpy as np
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        times = []
        times.append(releaseTimes[0])
        [times.append(releaseTimes[i] - releaseTimes[i-1]) for i in range(1,len(releaseTimes))]
        m = max(times)
        a = np.array(times)
        r = np.where(a==m)
        ans = np.array(list(keysPressed))
        ans = ans[r]
        ans = np.sort(ans)
        return ans[-1]