class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        HashMap<Integer,Integer> hs = new HashMap<Integer,Integer>();
        
        for(int i=0;i<nums.length;i++)
        {           
            if(hs.containsKey(target-nums[i]))
            {
                res[0] = hs.get(target-nums[i]);
                res[1] = i;
                return res;
            }
        hs.put(nums[i],i);
        }
    return res; 
    }
}