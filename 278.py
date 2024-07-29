def isBadVersion(version: int) -> bool:
    if version >= bad:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        first = 1
        last = n
        while first <= last:
            middle = (first + last) // 2
            if isBadVersion(middle) == False:
                first = middle + 1
            else:
                last = middle - 1
        return first


n = 5
bad = 4

solution = Solution()
result = solution.firstBadVersion(n)
print(result)