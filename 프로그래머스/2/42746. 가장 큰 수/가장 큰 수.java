import java.util.*;

class Solution {
    
    public String solution(int[] nums) {
        
        
        String[] stringNumbers = Arrays.stream(nums)
                    .mapToObj(String::valueOf)
                    .toArray(String[]::new);
        
        Arrays.sort(stringNumbers, (a, b) -> (b + a).compareTo(a + b));
        
        String result = "";
        for (String num : stringNumbers) {
            result += num;
        }
        
        if (result.charAt(0) == '0') {
            return "0";
        }
        return result;
    }
}