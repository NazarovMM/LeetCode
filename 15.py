class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # первое решение
        # for i in range(n):
        #     for j in range(n):
        #         for k in range(n):
        #             buff = sorted([nums[i], nums[j], nums[k]])
        #             if (nums[i]+nums[j]+nums[k] == 0) and (i != j and i != k and k != j):
        #                 if buff not in output:
        #                     output.append(buff)

        # второе решение
        output = set()
        negativ = []
        positiv = []
        zeros = []

        for num in nums:
            if num > 0:
                positiv.append(num)
            elif num < 0:
                negativ.append(num)
            else:
                zeros.append(num)

        n_set = set(negativ)
        p_set = set(positiv)

        # 1 случай, когда -1 1 0
        if zeros:
            for num in p_set:
                if -1*num in n_set:
                    output.add(tuple(sorted([-1*num, 0, num])))
        # 2 случай, когда 0 0 0
        if len(zeros) >= 3:
            output.add(tuple([0, 0, 0]))
        # 3 случай, когда 1 1 -2
        for i in range(len(positiv)-1):
            for j in range(i+1, len(positiv)):
                target = (-1)*(positiv[i]+positiv[j])
                if target in n_set:
                    output.add(tuple(sorted([positiv[i], positiv[j], target])))
        # 4 случай, когда -1 -1 2
        for i in range(len(negativ)-1):
            for j in range(i+1, len(negativ)):
                target = (-1)*(negativ[i]+negativ[j])
                if target in p_set:
                    output.add(tuple(sorted([negativ[i], negativ[j], target])))

        return output


nums = [1, 2, -2, -1]
solution = Solution()
result = solution.threeSum(nums)
print(result)
