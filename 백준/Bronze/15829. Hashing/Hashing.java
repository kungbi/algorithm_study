import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int l = sc.nextInt();
        String str = sc.next();

        int hash = 0;
        for(int i = 0; i < str.length(); i++){
            hash += (str.charAt(i) - 'a' + 1) * Math.pow(31, i);
        }
        System.out.println(hash % 1234567891);
    }
}