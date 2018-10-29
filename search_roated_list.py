class Solution:
    def searchRoatedList(self, nums, target):
        if not nums:
            return False
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid]==target or nums[left]==target or nums[right]==target:
                return True
            if mid+1>right or mid-1<left:
                return False
            if nums[mid]>target and nums[right]<target:
                right = mid-1
            else:
                return self.searchRoatedList(nums[left:mid], target) or self.searchRoatedList(nums[mid+1:right+1], target)
        return False

class Solution2:
    def searchRoatedList(self, nums, target):
        if not nums:
            return False
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid]==target or nums[left]==target or nums[right]==target:
                return True
            if nums[mid] == nums[right]:
                right -= 1
                continue
            if nums[mid]<nums[right]:
                if nums[mid]<target and nums[right]>target:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if nums[mid]>target and nums[right]<target:
                    right = mid-1
                else:
                    left = mid+1
        if (left<len(nums) and nums[left]==target) or (right>=0 and nums[right]==target):
            return True
        else:
            return False
    
nums = [1,3,1,1,1]
target = 3
s = Solution2()
print(s.searchRoatedList(nums, target))
                

