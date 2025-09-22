package ad;

import java.util.Scanner;

public class sum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of elements (n): ");
        int n = scanner.nextInt();
        if(n<0) {
        	System.out.println("invalid");
        	return;
        }
        int sum = 0;
        for (int i = 0; i < n+1; i++) {
        	sum+=i;
        }
        System.out.println("The sum of the " + n + " numbers is: " + sum);
        
    }
}