class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        solution = []
        for num in numbers:
            diff = target - num
            if diff in numbers:
                solution.append(numbers.index(num) + 1)
                solution.append(numbers.index(diff) + 1)
            if numbers.index(num) + 1 in solution:
                break  
        return solution    
        