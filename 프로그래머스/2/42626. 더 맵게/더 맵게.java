import java.util.*;
import java.util.stream.Collectors; 


class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> heap = new PriorityQueue(
            Arrays.stream(scoville).boxed().collect(Collectors.toList())
        );
        
        int result = 0;
        while (2 <= heap.size() && heap.peek() < K) {
            int a = heap.poll();
            int b = heap.poll();
            
            heap.add(a + b * 2);
            result++;
        }
        
        if (heap.peek() < K)
            return -1;
        return result;
    }
}