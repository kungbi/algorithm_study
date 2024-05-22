import java.util.*;
import java.lang.*;


class Solution {
    int answer = 0;
    char[] char_list = {'A', 'C', 'F', 'J', 'M', 'N','R', 'T'};
    
    public boolean isAnswer(String[] data, List<Character> currList) {
        for (String d : data) {
            int a = currList.indexOf(d.charAt(0));
            int b = currList.indexOf(d.charAt(2));
            int dist = Math.abs(a - b) - 1;
            int requiredDist = d.charAt(4) - '0';
            
            if (d.charAt(3) == '=') {
                if (dist != requiredDist) return false;
            } else if (d.charAt(3) == '<') {
                if (dist >= requiredDist) return false;
            } else if (d.charAt(3) == '>') {
                if (dist <= requiredDist) return false;
            }
        }
        return true;
    }
    
    public void f(String[] data, List<Character> currList, boolean[] visited, int n) {
        if (currList.size() == char_list.length) {

            if (isAnswer(data, currList))
                answer++;
            return ;
        }
        
        for (int i = 0; i < 8; i++) {
            if (visited[i] == false) {
                visited[i] = true;
                currList.add(char_list[i]);
                f(data, currList, visited, n - 1);
                currList.remove(currList.size() - 1);
                visited[i] = false;
            }
        }
    }
    
    public int solution(int n, String[] data) {
        boolean[] visited = new boolean[char_list.length];
        f(data, new ArrayList<>(), visited, n);
        return answer;
    }
}