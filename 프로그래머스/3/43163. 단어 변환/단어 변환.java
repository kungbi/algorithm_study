import java.util.*;

class Solution {
    public int countDiff(String a, String b) {
        int result = 0;
        
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                result++;
            }
        }
        
        return result;
    }
    
    class Node {
        String word;
        int count;
        
        Node(String word, int count) {
            this.word = word;
            this.count = count;
        }
    }
    
    public int solution(String begin, String target, String[] words) {
        Queue<Node> queue = new LinkedList();
        boolean[] visited = new boolean[words.length];
        
        queue.add(new Node(begin, 0));
        
        while (!queue.isEmpty()) {
            Node node = queue.remove();
            
            if (node.word.equals(target)) {
                return node.count;
            }
            
            for (int i = 0; i < words.length; i++) {
                if (countDiff(node.word, words[i]) != 1)
                    continue ;
                if (visited[i] == true)
                    continue ;
                
                queue.add(new Node(words[i], node.count + 1));
                visited[i] = true;
            }
        }
        
        return 0;
    }
}