class Solution:
    def isPossible(self, nums):
        freq = collections. Counter(nums)
        end = defaultdict(int)
        for i in nums:
           if freq[i] > 0:
                freq[i]-=1
                if end[i-1] > 0:
                   end[i-1]-=1
                   end[i]+=1
                elif freq[i+1] > 0 and freq[i+2] > 0:
                    freq[i+1]-=1
                    freq[i+2]-=1
                    end[i+2]+=1
                else:
                    return False
        return True