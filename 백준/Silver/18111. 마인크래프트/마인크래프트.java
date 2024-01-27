import java.io.*;
import java.util.*;

public class Main{

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int m = Integer.parseInt(line[1]);
        int b = Integer.parseInt(line[2]);

        int[][] map = new int[n][m];
        for (int i = 0; i < n; i++) {
            line = br.readLine().split(" ");
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(line[j]);
            }
        }

        int time, height, tmp, f1, f2, b_copy;
        int result_time = Integer.MAX_VALUE, result_height = 0;
        for (height = 0; height <= 256; height++) {
            f1 = 0;
            f2 = 0;
            b_copy = b;
            for (int y = 0; y < n; y++) {
                for (int x = 0; x < m; x++) {
                    tmp = Math.abs(map[y][x] - height);
                    if (height < map[y][x]) {
                        f1 += tmp;
                        b_copy += tmp;
                    } else if (map[y][x] < height) {
                        f2 += tmp;
                    }
                }
            }
            if (b_copy < f2) continue;

            time = f1 * 2 + f2;
            if (time <= result_time) {
                result_time = time;
                result_height = height;
            }
        }

        System.out.printf("%d %d\n", result_time, result_height);
    }
}