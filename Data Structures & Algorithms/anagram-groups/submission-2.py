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

        # group_anagram = {}
        # for s in strs:
        #     sort_s = "".join(sorted(s))

        #     if sort_s in group_anagram:
        #         group_anagram[sort_s].append(s)
        #     else:
        #         group_anagram[sort_s] = [s]

        # return list(group_anagram.values())

        #key as origal word and value and list of chars
        group = {}

        for s in strs:
            #list of 26 chars 
            chars = [0] * 26

            for c in s:
                # this gives the index of char within 26 chars
                chars[ord(c) - ord('a')] += 1

                #Since list if mutual and can't be a hash key, need to convert it to tuple
            key = tuple(chars)

                # now we have key like this [0, 0, 0, 0, ...... so now, placeholder of 26 chars]
            if key in group:
                group[key].append(s)
            else:
                group[key] = [s]
                
        return list(group.values())





        







       
        