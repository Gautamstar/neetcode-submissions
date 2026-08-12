class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatestElement = -1
        for i in range(len(arr)-1, -1,-1):
            curr = arr[i]
            arr[i] = greatestElement
            greatestElement = max(greatestElement, curr)
        return arr
        