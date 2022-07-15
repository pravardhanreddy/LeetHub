class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = [i for i in range(len(people))]
        people.sort()
        temp = [0] * len(people)
        prev = people[0][0] - 1
        prev_list = []
        for p in people:
            # print(p[0], p[1], ans, temp)
            if prev != p[0]:
                prev = p[0]
                while len(prev_list):
                    i = prev_list.pop()
                    ans.pop(i)
            prev_list.append(p[1])
            ind = ans[p[1]]
            temp[ind] = p
        return temp