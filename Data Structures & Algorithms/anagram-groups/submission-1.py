class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # what do I need remember?
         # need to remember each char as i loop through
        # what do I need to track?
         # need to keep track of chars
        # which data to use?
         # use hashmap key:value as sorted word : orginal words

        # Anagram is same len and same char
        # are upper and lower case char consider same or different?
        # what do we return with empty input?
        # are all input only alpabet?

        #input = ["cat", "tac", "mad"]
        #oupt = [["cat", "tac"], ["mad"]]

        group_anagram = {}
        for s in strs:
            sort_s = "".join(sorted(s))

            if sort_s in group_anagram:
                group_anagram[sort_s].append(s)
            else:
                group_anagram[sort_s] = [s]

        return list(group_anagram.values())







       
        