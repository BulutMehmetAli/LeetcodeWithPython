def isPalindrome(self, x: int) -> bool:
        x = str(x)
        size = len(x)
        size = size//2
        if x[:-size-1:-1] == x[:size]:
            return True
        else:
            return False
        