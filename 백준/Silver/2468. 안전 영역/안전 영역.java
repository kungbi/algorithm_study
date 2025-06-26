import java.util.*;
import java.io.*;
import java.math.*;

public class Main {

	static int[] dxs = {0, 1, 0, -1};
	static int[] dys = {-1, 0, 1, 0};

	public static class Pos {
		int x;
		int y;

		Pos(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	public static boolean isFrame(int x, int y, int n) {
		return (0 <= x && x < n) && (0 <= y && y < n);
	}

	public static void bfs(int map[][], boolean visited[][], int x, int y, int water) {
		int n = map.length;
		Queue<Pos> queue = new LinkedList<Pos>();
		queue.add(new Pos(x, y));
		visited[y][x] = true;

		while (!queue.isEmpty()) {
			Pos pos =  queue.poll();

			for (int i = 0; i < 4; i++) {
				int nx = pos.x + dxs[i];
				int ny = pos.y + dys[i];
				if (!isFrame(nx, ny, n)) continue;
				if (visited[ny][nx]) continue;
				if (map[ny][nx] <= water) continue;

				visited[ny][nx] = true;
				queue.add(new Pos(nx, ny));
			}	
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		int map[][] = new int[n][n];
		StringTokenizer st;
		for (int y = 0; y < n; y++) {
			st = new StringTokenizer(br.readLine());
			for (int x = 0; x < n; x++) {
				map[y][x] = Integer.parseInt(st.nextToken());
			}
		}

		int answer = 0;
		for (int water = 0; water <= 100; water++){
			boolean[][] visited = new boolean[n][n];
			int tmp = 0;
			for (int y = 0; y < n; y++) {
				for (int x = 0; x < n; x++) {
					if (!visited[y][x] && water < map[y][x]) {
						bfs(map, visited, x, y, water);
						tmp++;
					}
				}
			}
			answer = Math.max(answer, tmp);
		}
		System.out.println(answer);
	}
}