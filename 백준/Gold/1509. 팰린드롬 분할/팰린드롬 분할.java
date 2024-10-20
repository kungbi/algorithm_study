import java.io.*;
import java.util.*;

class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

		String input = bufferedReader.readLine();
		int n = input.length();

		int palindrom_dp[][] = new int[n][n];

		for (int size = 0; size < n; size++) {
			for (int start = 0; start < n; start++) {
				if (size == 0)
					palindrom_dp[start][start] = 1;
				else if (size == 1 && start + 1 < n) {
					if (input.charAt(start) == input.charAt(start + 1))
						palindrom_dp[start][start + 1] = 1;
				} else if (start + size < n) {
					if (input.charAt(start) == input.charAt(start + size)
						&& palindrom_dp[start + 1][start + size - 1] == 1)
						palindrom_dp[start][start + size] = 1;
				}
			}
		}

		int min_metrix[] = new int[n];
		Arrays.fill(min_metrix, Integer.MAX_VALUE);
		min_metrix[0] = 1;

		for (int end = 0; end < n; end ++) {
			for (int start = 0; start <= end; start++) {
				if (palindrom_dp[start][end] == 0)
					continue ;

				if (start == 0)
					min_metrix[end] = 1;
				else
					min_metrix[end] = Math.min(min_metrix[end], min_metrix[start - 1] + 1);
			}
		}

		System.out.println(min_metrix[n-1]);
	}
}