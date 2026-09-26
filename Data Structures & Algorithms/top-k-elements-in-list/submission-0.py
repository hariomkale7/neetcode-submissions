class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        new_lst = []
        for i in nums:
            if i in group:
                group[i] += 1
            else:
                group[i] = 1

        sorted_group = sorted(group.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            new_lst.append(sorted_group[i][0])

        return new_lst