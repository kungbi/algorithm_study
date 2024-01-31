import java.io.*;
import java.util.*;

public class Main {

    public static boolean isFrame(int n) {
        return 0 <= n && n <= 100000;
    }

    public static int bfs(int n, int k) {
        Queue<int[]> queue = new LinkedList<>();
        boolean[] visited = new boolean[100001];

        visited[k] = true;
        queue.add(new int[]{k, 0});

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int num = curr[0];
            int dist = curr[1];
            if (num == n) {
                return dist;
            }

            if (Math.abs(n - k) <= dist) {
                continue;
            }

            if (isFrame(num - 1) && visited[num - 1] == false) {
                visited[num - 1] = true;
                queue.add(new int[]{num - 1, dist + 1});
            }
            if (isFrame(num + 1) && visited[num + 1] == false) {
                visited[num + 1] = true;
                queue.add(new int[]{num + 1, dist + 1});
            }
            if (isFrame(num / 2) && num % 2 == 0 && visited[num / 2] == false) {
                visited[num / 2] = true;
                queue.add(new int[]{num / 2, dist + 1});
            }
        }
        return 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int k = Integer.parseInt(line[1]);

        System.out.println(bfs(n, k));
    }
}