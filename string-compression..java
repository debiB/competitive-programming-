class Solution {
    public int compress(char[] chars) {
    int length=0; 
    int i=0,j=i;
    while (i< chars.length){
        while(j< chars.length && chars[i] == chars[j]){
            j++;
        }
        chars[length++] = chars[i];
        if(j-i>1){
            String c= j-i+"";
            for(char cnt: c.toCharArray()){
                chars[length++] = cnt;
            }
        }
            i=j;
        }
        return length;
    }    
    }