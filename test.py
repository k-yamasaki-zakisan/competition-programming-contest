# nums1 = [2, 1, 3]
# nums2 = [10, 2, 5, 0]
# ans = 0
# for num1 in nums1:
#     for _ in range(len(nums2)):
#         ans ^= num1
# for num2 in nums2:
#     for _ in range(len(nums1)):
#         ans ^= num2
# print(ans)
ans = 1
print(ans ^ 2)
print(ans ^ 2 ^ 2)
print(ans ^ 2 ^ 2 ^ 2)
