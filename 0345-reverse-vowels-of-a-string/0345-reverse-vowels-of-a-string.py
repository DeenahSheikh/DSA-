class Solution:
    def reverseVowels(self, s: str) -> str:
        left=0
        right=len(s)-1
        vowels="aeiouAEIOU"
        s=list(s)

        while right>left:
            if s[left] not in vowels:
                left+=1
                continue
            if s[right] not in vowels:
                right-=1
                continue

            temp=s[left]
            s[left]=s[right]
            s[right]=temp

            left+=1
            right-=1

        return "".join(s)

                
