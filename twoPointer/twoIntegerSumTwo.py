def twoSum(self, numbers: List[int], target: int) -> List[int]:
    i = 0
    while i < len(numbers) -1:

        if i < len(numbers) -1 and target - numbers[i] > numbers[-1]:
            i +=1

        j = i+1

        while j < len(numbers):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            else:
                j +=1

        i +=1
            

def twoSumAns(numbers, target):
    i = 0
    j = len(numbers) -1

    while i < j:
        res = numbers[i] + numbers[j]
        if res > target:
            j -=1
        else:
            if res == target:
                return [i+1, j+1]
            i +=1
