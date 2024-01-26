import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long l = sc.nextInt();
        String str = sc.next();

        long hash = 0;
        long r = 1;
        int a;
        for(int i = 0; i < l; i++){
            a = str.charAt(i) - 'a' + 1;
            hash = (hash + (a * r) % 1234567891) % 1234567891;
            r = (r * 31) % 1234567891;
        }
        System.out.println(hash);
    }
}