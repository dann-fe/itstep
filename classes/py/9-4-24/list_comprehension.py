nums = [1, 2, 3, 4, 5]
nums2 = []
for i in nums:
    nums2.append(i * i)

print(nums2)

nums3 = [x ** 2 for x in nums if x > 3]  # list comprehension
print(nums3)

del nums3[0]

print(nums3)