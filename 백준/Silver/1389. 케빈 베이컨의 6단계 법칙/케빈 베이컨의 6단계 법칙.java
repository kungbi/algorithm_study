import java.io.*;
import java.util.*;

public class Main {

    public static int bfs(int[][] edge, int start) {
        Queue<int[]> queue = new LinkedList<>();
        boolean[] visited = new boolean[edge.length];

        visited[start] = true;
        queue.add(new int[]{start, 0});
        int count = 0;
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int currV = curr[0];
            int currD = curr[1];

            for (int i = 1; i < edge[currV].length; i++) {
                if (edge[currV][i] == 1 && visited[i] == false) {
                    count += currD + 1;
                    visited[i] = true;
                    queue.add(new int[]{i, currD + 1});
                }
            }
        }
        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int m = Integer.parseInt(line[1]);
        int[][] edge = new int[n + 1][n + 1];

        for (int i = 0; i < m; i++) {
            line = br.readLine().split(" ");
            int a = Integer.parseInt(line[0]);
            int b = Integer.parseInt(line[1]);

            edge[a][b] = 1;
            edge[b][a] = 1;
        }

        int minD = Integer.MAX_VALUE;
        int minI = 0;
        for (int i = 1; i <= n; i++) {
            int result = bfs(edge, i);
            if (result < minD) {
                minD = result;
                minI = i;
            }
        }
        System.out.println(minI);
    }
}