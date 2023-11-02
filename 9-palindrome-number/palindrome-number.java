class Solution {
    public boolean isPalindrome(int x) {
        String s = Integer.toString(x);
        int[] nums = new int[s.length()];
        int start =0,end=nums.length-1;
        
        for (int i = 0; i < nums.length; i++){
            nums[i] = s.charAt(i) - '0';
        }
        
        for (int j = 0; j < nums.length; j++){
            if(nums[start]!=nums[end]){
                return false ;
            }
            start ++;end--;
        }
        return true ;
        
        
    }
}