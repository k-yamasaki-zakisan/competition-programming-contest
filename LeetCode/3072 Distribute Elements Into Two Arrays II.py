from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        from array import array
        from bisect import bisect

        arr1 = [nums[0]]
        arr2 = [nums[1]]
        arr1_sort = array("I", [0, nums[0]])
        arr2_sort = array("I", [0, nums[1]])
        arr1_cnt = arr2_cnt = 1
        for i in range(2, len(nums)):
            arr1_tmp_i = bisect(arr1_sort, nums[i])
            arr2_tmp_i = bisect(arr2_sort, nums[i])
            if arr2_cnt - arr2_tmp_i < arr1_cnt - arr1_tmp_i:
                arr1_sort.insert(arr1_tmp_i, nums[i])
                arr1.append(nums[i])
                arr1_cnt += 1
            elif arr1_cnt - arr1_tmp_i < arr2_cnt - arr2_tmp_i:
                arr2_sort.insert(arr2_tmp_i, nums[i])
                arr2.append(nums[i])
                arr2_cnt += 1
            elif arr1_cnt - arr1_tmp_i == arr2_cnt - arr2_tmp_i:
                if arr2_cnt < arr1_cnt:
                    arr2_sort.insert(arr2_tmp_i, nums[i])
                    arr2.append(nums[i])
                    arr2_cnt += 1
                else:
                    arr1_sort.insert(arr1_tmp_i, nums[i])
                    arr1.append(nums[i])
                    arr1_cnt += 1
            else:
                arr1_sort.insert(arr1_tmp_i, nums[i])
                arr1.append(nums[i])
                arr1_cnt += 1
        return arr1 + arr2
