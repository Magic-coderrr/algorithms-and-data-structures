from collections import defaultdict


def groupAnagrams(strs):
        dictonary_anagram=defaultdict(list)

        for word in strs:
            sorted_word="".join(sorted(word))
            dictonary_anagram[sorted_word].append(word)
            
        return list(dictonary_anagram.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))