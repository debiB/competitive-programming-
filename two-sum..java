class Solution {
    public int[] twoSum(int[] nums, int target) {
       Map <Integer,Integer> s= new HashMap<>();
       
       for(int i=0;i<nums.length;i++){
           int comp= target-nums[i];
           if(s.containsKey(comp)){
             return new int [] {s.get(comp),i};
           }
           s.put(nums[i],i);

       }
       throw new IllegalArgumentException("no two values add up to the target");
    }
}