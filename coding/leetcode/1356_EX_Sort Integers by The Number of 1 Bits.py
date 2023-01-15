class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda num: (self.count_bits(num), num))
        return arr

    def count_bits(self, num: int) -> int:
        count = 0
        while num:
            num &= num - 1
            count += 1
        return count
