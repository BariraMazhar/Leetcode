def longest_palindrome_substring(s):
    start=0
    max_len=0
    for i in range(len(s)):     #outer loop
        low=i-1                 #for odd number substring
        high=i+1
        while(low>=0 and high<len(s) and s[low]==s[high]):
            max_len=high-low+1
            start=low
        
        low=i                    #for even number substring
        high=i+1
        while(low>=0 and high<len(s) and s[low]==s[high]):
            max_len=high-low+1
            start=low
        
        return(s[start:start+max_len])


        a=longest_palindrome_substring("dabad")
        print(a)