from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_high = height[left]
        right_high = height[right]


        max_area = min(left_high, right_high) * (right - left)

        while left < right:
            if left_high < right_high:
                while left_high >= height[left] and right>left:
                    left += 1
                left_high = height[left]
            else:
                while right_high >= height[right] and right>left:
                    right -= 1
                right_high = height[right]
            max_area = max(max_area, min(left_high, right_high) * (right - left))
        
        return max_area
    
if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    print(solution.maxArea(height))  