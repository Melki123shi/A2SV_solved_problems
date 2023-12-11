class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dictionary = {}
        for path in paths:
            first, *array = path.split()
            cat = []
            for arr in array:
                cat = arr.split('(')
                if (cat[1][:-1]) not in dictionary:
                    dictionary[cat[1][:-1]] = [first + '/' + cat[0]]
                else:
                    dictionary[cat[1][:-1]].append(first + '/' + cat[0])
        paths = []
        for key in dictionary:
            if len(dictionary[key]) > 1:
                paths.append(dictionary[key])
        return paths

        
