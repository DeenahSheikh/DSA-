class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        left=0
        right=len(s)-1

        while right> left:
            if not s[left].isalpha():
                left+=1
                continue
            if not s[right].isalpha():
                right-=1
                continue
            
            temp=s[left]
            s[left]=s[right]
            s[right]=temp

            left+=1
            right-=1

        return "".join(s)