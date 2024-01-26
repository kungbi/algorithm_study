import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        int num;

        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < k; i++) {
            num = sc.nextInt();
            if (num == 0) {
                stack.pop();
            } else {
                stack.add(num);
            }
        }

        int result = 0;
        for (int i = 0; i < stack.size(); i++) {
            result += stack.get(i);
        }
        System.out.println(result);
    }
}