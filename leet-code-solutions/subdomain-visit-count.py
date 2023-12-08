class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dictionary = {}
        for cp in cpdomains:
            count, string = cp.split()
            strings = string.split('.')
            while strings != []:
                if '.'.join(strings) not in dictionary:
                    dictionary['.'.join(strings)] = int(count)
                else:
                    dictionary['.'.join(strings)] += int(count)
                strings.pop(0)
        cpdomains = []
        for key in dictionary:
            cpdomains.append(str(dictionary[key]) + ' ' + key)
        return cpdomains
            