class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans

nums = [5,0,1,2,3,4]

solution = Solution()
result = solution.buildArray(nums)
print(result)