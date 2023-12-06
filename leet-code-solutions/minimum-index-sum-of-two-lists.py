class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dictionary1 = {}
        dictionary2 = {}
        for i,l1 in enumerate(list1):
            dictionary1[l1] = i
          
        for i,l2 in enumerate(list2):
            dictionary2[l2] = i

        list1 = dictionary1 
        list2 = dictionary2

        del dictionary1
        del dictionary2

        result = []
        m = float('inf')
        for string in list1:
            if (string in list2) and (list1[string] + list2[string] <= m):
                if type(m) != float and list1[string] + list2[string] < m:
                    result = []
                result.append(string)
                m = list1[string] + list2[string]
        return result
