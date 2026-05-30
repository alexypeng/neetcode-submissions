class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = {}

        for i in s:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1
        
        for i in t:
            if i not in store or store[i] == 0:
                return False
            store[i] -= 1
        
        for i in store:
            if store[i] != 0:
                return False

        return True