class Solution:
    def rotate(self, A: List[int], k: int) -> None:
        def reverse(i, j):
            while i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        n = len(A)
        k %= n
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
