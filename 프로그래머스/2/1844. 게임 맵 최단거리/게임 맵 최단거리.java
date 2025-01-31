import java.util.*;

class Solution {
    class Pos {
        int x;
        int y;
        int cost;
        
        Pos(int x, int y, int c) {
            this.x = x;
            this.y = y;
            this.cost = c;
        }
    }
    
    int[] dxs = {0, -1, 0, 1};
    int[] dys = {-1, 0, 1, 0};
    
    boolean isFrame(int x, int y, int n, int m) {
        return 0 <= x && x < m && 0 <= y && y < n;
    }
    
    public int solution(int[][] maps) {
        boolean[][] visited = new boolean[maps.length][maps[0].length];
        
        Queue<Pos> queue = new LinkedList();
        queue.add(new Pos(0, 0, 1));
        
        while (!queue.isEmpty()) {
            Pos pos = queue.poll();
            
            if (pos.x == maps[0].length - 1 && pos.y == maps.length - 1) {
                return pos.cost;
            }
            
            for (int i = 0; i < 4; i++) {
                int dx = dxs[i];
                int dy = dys[i];
                
                int nx = pos.x + dx;
                int ny = pos.y + dy;
                
                if (isFrame(nx, ny, maps.length, maps[0].length) == false) {
                    continue;
                }
                if (visited[ny][nx] == true) {
                    continue;
                }
                if (maps[ny][nx] == 0) {
                    continue;
                }
                
                visited[ny][nx] = true;
                queue.add(new Pos(nx, ny, pos.cost + 1));
            }
        }
        
        return -1;
    }
}