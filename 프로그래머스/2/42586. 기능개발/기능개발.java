import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<Integer> durations = new LinkedList();
        
        for (int i = 0; i < progresses.length; i++) {
            durations.add((int) Math.ceil((100.0 - progresses[i]) / speeds[i]));
        }
        
        int days = 0;
        List<Integer> results = new ArrayList();
        
        
        while (!durations.isEmpty()) {
            Integer duration = durations.poll();
            
            if (days < duration) {
                results.add(1);
                days = duration;
            } else {
                results.set(results.size() - 1, results.get(results.size() - 1) + 1);
            }

        }
        
        return results
                .stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}