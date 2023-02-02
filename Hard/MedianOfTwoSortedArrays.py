class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lenght1 = 0
        lenght2 = 0
        index=0
        arr= []
        if (len(nums1)+len(nums2))%2==0:
            mid = int((len(nums1)+len(nums2))/2)
            while lenght1<len(nums1) and lenght2<len(nums2):
                if nums1[lenght1]<nums2[lenght2]:
                    arr.append(nums1[lenght1])
                    index+=1
                    lenght1+=1
                else:
                    arr.append(nums2[lenght2])
                    index+=1
                    lenght2+=1
            while lenght1<len(nums1):
                arr.append(nums1[lenght1])
                lenght1+=1
            while lenght2<len(nums2):
                arr.append(nums2[lenght2])
                lenght2+=1
            return (arr[mid]+arr[mid-1])/2
        else:
            mid = int((len(nums1)+len(nums2))/2)
            while lenght1<len(nums1) and lenght2<len(nums2):
                if nums1[lenght1]<nums2[lenght2]:
                    arr.append(nums1[lenght1])
                    index+=1
                    lenght1+=1
                else:
                    arr.append(nums2[lenght2])
                    index+=1
                    lenght2+=1
            while lenght1<len(nums1):
                arr.append(nums1[lenght1])
                lenght1+=1
            while lenght2<len(nums2):
                arr.append(nums2[lenght2])
                lenght2+=1
            return (arr[mid])

        
