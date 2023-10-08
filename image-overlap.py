class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
            i1 = []
            i2 = []
            for i in range(len(img1)):
                num1 = int("0b" +  "".join(map(str, img1[i])), 2)
                num2 = int("0b" +  "".join(map(str, img2[i])), 2)   
                i1.append(num1)
                i2.append(num2)
            q = deque([(i1, (0,0))])    
            visited = set((0,0))
            _max = 0
            while q:
                num, co = q.popleft()
                if all([True if b==0 else False for b in num]):
                    continue
                over = 0
                for i in range(len(img1)):
                    over+=(num[i]&i2[i]).bit_count()
                _max = max(_max, over)
                if(co[0]+1, co[1]) not in visited:
                    right = [b//2 for b in num]
                    q.append((right, (co[0]+1, co[1])))
                    visited.add((co[0]+1, co[1]))
                if(co[0]- 1, co[1]) not in visited:
                    left = [(2*b & ~(1<<(len(img1)+1))) for b in num]
                    q.append((left, (co[0]- 1, co[1])))
                    visited.add((co[0]- 1, co[1]))
                if (co[0], co[1]+1) not in visited:
                    up = [0] + num[:-1]
                    q.append((up,(co[0], co[1]+1)))
                    visited.add((co[0], co[1]+1))
                if (co[0], co[1]-1) not in visited:
                    down = num[1:] +[0]
                    q.append((down,(co[0], co[1]-1)))
                    visited.add((co[0], co[1]-1))
            return _max