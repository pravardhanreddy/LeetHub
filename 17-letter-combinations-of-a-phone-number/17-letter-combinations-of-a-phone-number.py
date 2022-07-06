class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return ''
        d = dict()
        d['2'] = 'abc'
        d['3'] = 'def'
        d['4'] = 'ghi'
        d['5'] = 'jkl'
        d['6'] = 'mno'
        d['7'] = 'pqrs'
        d['8'] = 'tuv'
        d['9'] = 'wxyz'
        
        prv, nxt = [], []
        for letter in d[digits[0]]:
            prv.append(letter)
        
        for i in range(1, len(digits)):
            for letter in d[digits[i]]:
                for cmb in prv:
                    nxt.append(cmb + letter)
            prv = nxt
            nxt = []
        return prv
        