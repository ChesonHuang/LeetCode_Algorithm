class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        #solution one:
        A =[str(x) for x in A]
        return [int(x) for x in str(int(''.join(A)) + K)]