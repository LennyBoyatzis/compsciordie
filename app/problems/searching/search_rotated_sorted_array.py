from typing import List


def search_rotated_array(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[mid] >= nums[left]:
            # LHS is normal
            # RHS is rotated
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # LHS is rotated
            # RHS is normal
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1


if __name__ == '__main__':
    # nums = [4,5,6,7,0,1,2]
    # target = 0

    nums = [5, 1, 3]
    target = 5 
    res = search_rotated_array(nums, target)
    print(f'res -> {res}')
