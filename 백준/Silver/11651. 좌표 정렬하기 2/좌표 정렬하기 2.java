import java.util.*;

public class Main {
    static class Pair implements Comparable<Pair>{
        int x;
        int y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Pair o) {
            if (this.y != o.y) {
                return this.y - o.y;
            }

            return this.x - o.x;
        }

        @Override
        public String toString() {
            return String.format("%d %d", this.x, this.y);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        List<Pair> arr = new ArrayList<>();

        int x, y;
        for(int i = 0; i < n; i++){
            x = sc.nextInt();
            y = sc.nextInt();
            arr.add(new Pair(x, y));
        }

        Collections.sort(arr);
        for(Pair pair : arr){
            System.out.println(pair.toString());
        }
    }
}