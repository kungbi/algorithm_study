import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int[] arr = new int[3];
        arr[0] = Integer.parseInt(line[0]);
        arr[1] = Integer.parseInt(line[1]);
        arr[2] = Integer.parseInt(line[2]);
        int n = Integer.parseInt(line[3]);

        for (int i = 0; i <= 300; i++) {
            for (int j = 0; j <= 300; j++) {
                for (int l = 0; l <= 300; l++) {
                    if (arr[0] * i + arr[1] * j + arr[2] * l == n) {
                        System.out.println(1);
                        return;
                    }
                }
            }
        }
        System.out.println(0);
    }
}