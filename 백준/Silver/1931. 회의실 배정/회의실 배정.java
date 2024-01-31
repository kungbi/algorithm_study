import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<long[]> meetingList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split(" ");
            long start = Integer.parseInt(line[0]);
            long end = Integer.parseInt(line[1]);
            meetingList.add(new long[]{start, end});
        }

        meetingList.sort((a, b) -> {
            if (a[1] != b[1]) {
                return Math.toIntExact(a[1] - b[1]);
            }
            return Math.toIntExact(a[0] - b[0]);
        });
        int count = 0;
        long curr = 0;
        for (long[] meeting : meetingList) {
            if (curr <= meeting[0]) {
                curr = meeting[1];
                count++;
            }
        }
        System.out.println(count);
    }
}