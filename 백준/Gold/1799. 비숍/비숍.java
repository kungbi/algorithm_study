import java.io.*;
import java.util.*;

class Main {
	static int result;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		int map[][] = new int[n][n];
		for (int y = 0; y < n; y++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int x = 0; x < n; x++) {
				map[y][x] = Integer.parseInt(st.nextToken());
			}
		}

		int mem[][] = new int[n][n];
		f(map, mem, 0, 0, n);
		System.out.println(result);
	}

	public static int isValid(int[][] map, int x, int y, int n) {
		if (map[y][x] == 0)
			return 0;

		for (int i = 1; i < n; i++) {
			if (!(0 <= y - i && 0 <= x - i))
				break ;
			if (map[y - i][x - i] == 2)
				return 0;
		}
		return 1;
	}


	public static void f(int[][] map, int [][] mem, int i, int count, int n) {
		if (i == n * 2) {
			result = Math.max(result, count);
			return ;
		}

		for (int x = 0; x < n; x++) {
			int y = i - x;
			if (!(0 <= y && y < n))
				continue ;


			if (isValid(map, x, y, n) == 1) {
				if (count + 1 < mem[y][x])
					continue ;

				mem[y][x] = count + 1;
				map[y][x] = 2;
				f(map, mem, i + 1, count + 1, n);
				map[y][x] = 1;
			}
		}
		f(map, mem, i + 1, count, n);

	}
}