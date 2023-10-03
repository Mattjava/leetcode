class Solution:
    def numIdenticalPairs(self, nums):
        good_pair_count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    good_pair_count += 1

        return good_pair_count
