# BSCS 4th Semester, Roll-no: BSCS-KC-011
# Task 2

nums = []
print("Enter 10 numbers:")

for i in range(10):
    random = int(input("Number:", i+1))
    nums.append(random)

odd_list = []
even_list = []

for num in nums:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("Original List:", nums)
print("Even Numbers:", even_list)
print("Odd Numbers:", odd_list)
