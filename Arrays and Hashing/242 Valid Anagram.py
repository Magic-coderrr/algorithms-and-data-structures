def isValidAnagram(s,t):
    # if length of s and t are different they cant be Anagrams
    if len(s) != len(t):
        return False
    
    countS,countT={},{}
    for i in range(len(s)):
        countS[s[i]]=countS.get(s[i],0)+1
        countT[t[i]]=countT.get(t[i],0)+1

    # if frequency and keys dont match the ans will be false else true

    return countS==countT
    

s="anagram"
t="nagaram"
print(isValidAnagram(s,t))