class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        table={}
        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1
        print(table)
        return 0
