class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        dce = []
        ans = 0
        for i in range(len(nums1)):
            dce.append(nums1[i] - nums2[i])
        def merges(left, right):
            li = []
            i,j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    li.append(left[i])
                    i+=1
                else:
                    li.append(right[j])
                    j+=1
            if i < len(left):
                li.extend(left[i:])
            if j < len(right):
                li.extend(right[j:])
            return li
        def merge(left, right):
            nonlocal ans
            if left == right:
                return [dce[left]]
            mid = (left+ right) // 2 
            l = merge(left, mid)
            r = merge(mid+1,right)
            a,b = 0,0 
            while a < len(l) and b < len(r):
                while a <= len(l)-1 and l[a] <= r[b] + diff:
                   a+=1
                if a == len(l):
                    ans+=(len(r)- b)*a
                    break
                else:
                    ans+=a
                b+=1
            return merges(l,r)
        
        merge(0, len(nums1)- 1)
        return ans