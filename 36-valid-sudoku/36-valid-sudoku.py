class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        # check sub box
        for i in range(0, 9, 3):
            for j in range(0,9,3):
                s = set()
                for p in range(3):
                    for q in range(3):
                        ele = board[i+p][j+q]
                        if ele == '.':
                            continue
                        if 1 <= int(ele) <= 9 and int(ele) not in s:
                            s.add(int(ele))
                        else:
                            return False
                        
        # check rows
        for i in range(9):
            s = set()
            for j in range(9):
                ele = board[i][j]
                if ele == '.':
                    continue
                if 1 <= int(ele) <= 9 and int(ele) not in s:
                    s.add(int(ele))
                else:
                    return False
                    
        # check rows
        for j in range(9):
            s = set()
            for i in range(9):
                ele = board[i][j]
                if ele == '.':
                    continue
                if 1 <= int(ele) <= 9 and int(ele) not in s:
                    s.add(int(ele))
                else:
                    return False
        return True