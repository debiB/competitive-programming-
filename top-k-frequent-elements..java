class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap();
        for(int n : nums){
            map.put(n,map.getOrDefault(n,0) + 1);//storing num and its freq
        }
        PriorityQueue<Integer> p = new PriorityQueue<>((a,b)->map.get(b) - map.get(a));
        p.addAll(map.keySet());
        int[] res = new int[k];
        for(int i = 0;i<k;i++){
            res[i] = p.remove();
        }
        return res;
    }
}