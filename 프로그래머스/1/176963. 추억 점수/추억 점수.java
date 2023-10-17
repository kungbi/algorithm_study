import java.util.Arrays;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        int index;
        
        for(int i = 0; i < photo.length; i++){
            for(String photo_name : photo[i]){
                index = Arrays.asList(name).indexOf(photo_name);
                if(index != -1){
                    answer[i] += yearning[index];
                }
            }
        }
        
        return answer;
    }
}