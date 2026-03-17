from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # deafult dictionary is made to make a default dictionary to store key and values
        anagrams_dict = defaultdict(list)
        for s in strs:
            # giving all the alphabets a count 0
            count = [0] * 26
            for c in s:
                # gives the number of times an alphabet occurs
                count[ord(c) - ord('a')] += 1
            # converts the key to tuple because a dictionary cant be stored in a list
            key = tuple(count)
            # append the string in the dictionary that is an anagram
            anagrams_dict[key].append(s)
        return list(anagrams_dict.values())
