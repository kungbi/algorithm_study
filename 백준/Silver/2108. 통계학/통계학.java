import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);

        int avg, sum = 0, med, min, max;
        Map<Integer, Integer> counter = new HashMap<>();
        min = arr[0];
        max = arr[n -1];
        med = arr[n / 2];

        int tmp, max_freq = 0;
        for (int num : arr) {
            sum += num;
            tmp = counter.getOrDefault(num, 0) + 1;
            counter.put(num, tmp);
            max_freq = Math.max(max_freq, tmp);
        }
        avg = Math.round((float) sum / n);

        List<Integer> list = new ArrayList<>();
        for (int num : counter.keySet()) {
            if (counter.get(num) == max_freq) {
                list.add(num);
            }
        }
        list.sort(Comparator.naturalOrder());

        System.out.println(avg);
        System.out.println(med);
        System.out.println(list.size() == 1? list.get(0): list.get(1));
        System.out.println(max - min);
    }
}