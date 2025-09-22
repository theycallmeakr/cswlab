package ad;

import java.util.Scanner;

public class fact {

    public static int factorial(int n) {
        if (n <= 1) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = scanner.nextInt();
        if (n < 0) {
            System.out.println("Negative");
            return;
        }
        System.out.println("Factorial of " + n + " is " + factorial(n));
    }
}
