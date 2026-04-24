class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # BS on rows then over the row that contains the sol


        rowIdx = binarySearchCol(matrix, target)
        if rowIdx == -1:
            return False

        return binarySearchRow(matrix[rowIdx], target)



def binarySearchRow(arr, target):
    low = 0
    high = len(arr)

    while low <= high:
        mid = (high + low) // 2
        curr = arr[mid]

        if curr == target:
            return True
        elif curr > target:
            high = mid - 1
        else:
            low = mid + 1
    return False

def binarySearchCol(grid, target):

    low = 0
    high = len(grid) - 1
    
    while low <= high:
        mid = (high + low) //2
        lb = grid[mid][0]
        ub = grid[mid][-1]

        if target >= lb and target <= ub:
            return mid
        elif target < lb:
            high = mid - 1
        else:
            low = mid + 1

    return -1

        