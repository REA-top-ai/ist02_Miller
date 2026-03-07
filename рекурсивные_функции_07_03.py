#1 (через рекурсию)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))


#1.1 (без нее)
def factorial(n):
    x = 1
    for n in range(1, n+1):
        x *= n
    return x

print(factorial(5))


#2 (без нее)
def numbers(nums):
    r = []
    for n in nums:
        r.append(n**2)
    return r

print(numbers([1,2,3,4,5]))


#2.1 (через рекурсию)
def numbers(nums):
    if nums == []:
        return []

    return [nums[0]**2] + numbers(nums[1:])
print(numbers([1,2,3,4,5]))