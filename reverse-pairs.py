class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        def merger(left, right): 
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
                return [nums[left]]
            mid = (left+right) //2
            le = merge(left,mid)
            ri = merge(mid+1, right)
            a,b = 0, 0
            while a < len(le) and b < len(ri):
                while a< len(le) and le[a] <= 2*ri[b]:
                    a+=1
                if a != len(le):
                    ans += len(le) - a
                else:
                    break
                b+=1
            return merger(le, ri)
        merge(0, len(nums)-1)
        return ans