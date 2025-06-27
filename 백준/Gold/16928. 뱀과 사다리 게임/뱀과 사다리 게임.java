import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int[] ladders = new int[101];
		int[] snakes = new int[101];
		
		for (int i = 0; i < N; i ++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			ladders[a] = b;
		}
		for (int i = 0; i < M; i ++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			snakes[a] = b;
		}

		Queue<int[]> queue = new LinkedList<int[]>();
		boolean[] visited = new boolean[101];
		int[] costs = new int[101];
		Arrays.fill(costs, Integer.MAX_VALUE);
		queue.add(new int[]{1, 0});
		visited[1] = true;

		while (!queue.isEmpty()) {
			int[] data = queue.poll();
			int current = data[0];
			int cost = data[1];

			if (costs[current] < cost) {
				continue;
			}

			for (int i = 1; i <= 6; i++) {
				int nextPosition = current + i;
				if (100 < nextPosition)
					continue;

				if (snakes[nextPosition] != 0) nextPosition = snakes[nextPosition];
				if (ladders[nextPosition] != 0) nextPosition = ladders[nextPosition];
				if (cost + 1 < costs[nextPosition]) {
					costs[nextPosition] = cost + 1;
					queue.add(new int[]{nextPosition, cost + 1});
				}
			}
		}
		
		// for (int i = 0; i <= 100; i++) {
		// 	System.out.print(costs[i] + " ");
		// }
		System.out.println(costs[100]);
	}
}