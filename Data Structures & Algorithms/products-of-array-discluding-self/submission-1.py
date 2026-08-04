class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Output = []
        for i in nums[:]:
            nums.remove(i)
            Output.append(math.prod(nums))
            nums.append(i)
        return Output    
     

        