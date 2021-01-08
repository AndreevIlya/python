def sum_two_biggest(num1, num2, num3):
    max1 = max(num1, num2, num3)
    nums = [num1, num2, num3]
    nums.remove(max1)
    max2 = max(nums)
    return max1 + max2


a, b, c = int(input("First: ")), int(input("Second: ")), int(input("Third: "))
print(sum_two_biggest(a, b, c))