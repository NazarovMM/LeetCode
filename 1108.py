class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


address = "255.100.50.0"
solution = Solution()
result = solution.defangIPaddr(address)
print(result)
