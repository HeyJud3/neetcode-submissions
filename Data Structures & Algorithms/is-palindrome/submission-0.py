class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        a = list(s)
        a.reverse()
        res = "".join(a)
        print(res)

        if s == res:
            return True

        return False