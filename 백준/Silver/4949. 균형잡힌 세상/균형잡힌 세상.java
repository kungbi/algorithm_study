import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;

        while(true){
            line = br.readLine();
            if(line.equals("."))
                break;

            Stack<Character> stack = new Stack<>();
            char c;
            boolean result = true;
            for (int i = 0; i < line.length(); i++) {
                c = line.charAt(i);
                if (c =='('){
                    stack.add('(');
                } else if (c == '[') {
                    stack.add('[');
                } else if (c == ')') {
                    if (stack.empty() || stack.pop() != '(') {
                        result = false;
                        break;
                    }
                } else if (c == ']') {
                    if (stack.empty() || stack.pop() != '[') {
                        result = false;
                        break;
                    }
                }
            }
            if (result && stack.empty()) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            }
        }
    }
}