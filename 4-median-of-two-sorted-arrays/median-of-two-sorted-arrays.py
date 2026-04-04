class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        def mergeArray(nums1, nums2):
            i, j = 0, 0
            merged = []

            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1

            # Add remaining elements
            merged.extend(nums1[i:])
            merged.extend(nums2[j:])

            return merged

        merged = mergeArray(nums1, nums2)
        n = len(merged)

        # Find median
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0