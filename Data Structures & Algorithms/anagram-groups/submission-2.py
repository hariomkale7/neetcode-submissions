class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = {}
        for item in strs:
            sort = "".join(sorted(item))
            if sort in group:
                group[sort].append(item)
            else:
                group[sort] = [item]

        return list(group.values())

