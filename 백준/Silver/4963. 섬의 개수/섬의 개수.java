import java.util.*;
import java.io.*;

public class Main {

	public static boolean isFrame(int x, int y, int w, int h) {
		return 0 <= x && x < w && 0 <= y && y < h;
	}

	static int[] dxs = {-1, 0, 1, 1, 1, 0, -1, -1};
	static int[] dys = {-1, -1, -1, 0, 1, 1, 1, 0};

	public static void solution(int[][] map, boolean[][] visited, int y, int x, int w, int h) {
		visited[y][x] = true;

		for (int i = 0; i < dxs.length; i++) {
			int dx = dxs[i];
			int dy = dys[i];
			int nx = x + dx;
			int ny = y + dy;

			if (isFrame(nx, ny, w, h) == false) {
				continue;
			}
			if (visited[ny][nx] == true) {
				continue;
			}
			if (map[ny][nx] == 0) {
				continue;
			}

			solution(map, visited, ny, nx, w, h);
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		while (true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int w = Integer.parseInt(st.nextToken());
			int h = Integer.parseInt(st.nextToken());
			if (w == 0 && h == 0) {
				break;
			}

			int[][] map = new int[h][w];
			for (int y = 0; y < h; y++) {
				st = new StringTokenizer(br.readLine());
				for (int x = 0; x < w; x++) {
					map[y][x] = Integer.parseInt(st.nextToken());
				}
			}

			boolean[][] visited = new boolean[h][w];
			int result = 0;
			for (int y = 0; y < h; y++) {
				for (int x = 0; x < w; x++) {
					if (visited[y][x] == false && map[y][x] == 1) {
						solution(map, visited, y, x, w, h);
						result++;
					}
				}
			}

			System.out.println(result);
		}

	}
}