class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        valuesIndex = defaultdict(list)

        for ind, val in enumerate(nums):
            valuesIndex[val].append(ind)
        
        for k, v in valuesIndex.items():
            currList = v
            totalSum = sum(v)

            prefixSum, restSum = 0, 0

            for i in range(len(v)):
                restSum = totalSum - prefixSum - v[i]

                leftSum = (v[i]*i) - prefixSum
                rightSum = restSum - (v[i]*(len(v) - i - 1))

                ans[v[i]] = leftSum + rightSum

                prefixSum += v[i]

        
        return ans