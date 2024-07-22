class Solution:
    def triangleType(self, nums: list[int]) -> str:
        a = nums[0]
        b = nums[1]
        c = nums[2]
        if a + b > c and a + c > b and b + c > a:
            if a != b and a != c and b != c:
                return "scalene"
            elif a == b == c:
                return "equilateral"
            else:
                return "isosceles"
        else:
            return "none"


nums = [8, 4, 4]
solution = Solution()
result = solution.triangleType(nums)
print(result)
