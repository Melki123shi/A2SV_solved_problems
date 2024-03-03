class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dictionary = defaultdict(int)
        for row in range(len(word)):
            for col in range(len(word[0])):
                  dictionary[word[row][col]] += 1
    

        # Check the existance of every number in the dictionary
        dict_word = Counter(word)
        for char in dict_word:
            if char not in dictionary:
                return False
            
            if dict_word[char] > dictionary[char]:
                return False
            
        path = set()
        def dfs(index, row, col):
            if index == len(word):
                return True
            
            if (col < 0 or row < 0
                or col >= len(board[0]) or row >= len(board)
                or board[row][col] != word[index] or
                (row, col) in path
            ):
                return False
            
            path.add((row, col))
            result = (
                dfs(index + 1, row + 1, col) or
                dfs(index + 1, row - 1, col) or
                dfs(index + 1, row, col + 1) or
                dfs(index + 1, row, col - 1) 
            )
            path.remove((row, col))

            return result
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(0, row, col):
                    return  True
        return False