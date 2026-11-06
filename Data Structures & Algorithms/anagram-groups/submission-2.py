class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # when accessing a any key it will default and create a list
        for s in strs: # for every string in the list
            count = [0]*26 # creates a list of 26 zeros (on for each letter in the alfabet)

            for c in s: # for every character in the string
                count[ord(c) - ord("a")] += 1  
                # were gonna determine what position of the     
                # dictionary of the current character and
                # we are gonna increment the count of the 
                # character by one
            res[tuple(count)].append(s)
            # we make the list into a tuple that cannot be modified
            # we want to append all the strings with the same tuple together
        return list(res.values())
