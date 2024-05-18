import java.util.*;
import java.lang.*;

class Solution {
    private static final int[] dx = {0, 0, -1, 1};
    private static final int[] dy = {-1, 1, 0, 0};
    
    public boolean isFrame(int x, int y, int n, int m) {
        return (0 <= x && x < m) && (0 <= y && y < n);
    }
    
    public int bfs(int[][] picture, int sx, int sy, boolean[][] visited, int n, int m){
        Queue<int[]> q = new LinkedList();
        q.add(new int[]{sx, sy});
        int size = 1;
        int curNum = picture[sy][sx];
        visited[sy][sx] = true;
        
        while (!q.isEmpty()) {
            int[] curPos = q.poll();
            int x = curPos[0];
            int y = curPos[1];

            for (int dir = 0; dir < 4; dir++) {
                int nx = x + dy[dir];
                int ny = y + dx[dir];
                
                if (isFrame(nx, ny, n, m) && visited[ny][nx] == false && picture[ny][nx] == curNum) {
                    q.add(new int[]{nx, ny});
                    visited[ny][nx] = true;
                    size++;   
                }
            }
        }
        return size;
    }
    
    public int[] solution(int m, int n, int[][] picture) {
        int tmp = n;
        n = m;
        m = tmp;
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        boolean[][] visited = new boolean[n][m];
        
        int size = 0;
        int[] answer = new int[2];
        
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < m; x++) {
                if (visited[y][x] == false && picture[y][x] != 0) {
                    numberOfArea++;
                    size = bfs(picture, x, y, visited, n, m);
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, size);
                }
            }
        }
        
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}