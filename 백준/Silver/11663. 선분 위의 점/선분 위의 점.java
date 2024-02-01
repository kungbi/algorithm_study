import java.io.*;
import java.util.*;

public class Main {

    public static int searchIndex(int[] dots, int num, String d) {
        int start = 0;
        int end = dots.length - 1;
        int result = -1;

        int mid = 0;
        while (start <= end) {
            mid = (start + end) / 2;
            if (d.equals("start")) {
                if (dots[mid] < num) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            } else {
                if (dots[mid] > num) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            }
        }

        if (d.equals("start")) {
            result = start;
        } else {
            result = end;
        }

       return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);
        int[] dots = new int[n];
        int[][] lines = new int[m][2];

        input = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            int dot = Integer.parseInt(input[i]);
            dots[i] = dot;
        }

        for (int i = 0; i < m; i++) {
            input = br.readLine().split(" ");
            int start = Integer.parseInt(input[0]);
            int end = Integer.parseInt(input[1]);
            lines[i][0] = start;
            lines[i][1] = end;
        }

        Arrays.sort(dots);
        for (int[] line : lines) {
            int start = line[0];
            int end = line[1];

            int startDotIndex = searchIndex(dots, start, "start");
            int endDotIndex = searchIndex(dots, end, "end");
            if (endDotIndex - startDotIndex < 0) {
                System.out.println(0);
            } else {
                System.out.println(endDotIndex - startDotIndex + 1);
            }
        }
    }
}