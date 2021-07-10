package numbers;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a natural number: ");
        int number = scan.nextInt();
        if (number > 0 && number % 2 != 0) {  // check for Odd and Buzz
            System.out.println("This number is Odd.");
            if (number % 10 == 7 && number % 7 == 0) {  // divisible and ends with 7
                System.out.println("It is a Buzz number.");
                System.out.println("Explanation:");
                System.out.println(number + " is divisible by 7 and ends with 7");
            } else if (number % 10 == 7) {  // ends with 7
                System.out.println("It is a Buzz number.");
                System.out.println("Explanation:");
                System.out.println(number + " ends with 7");
            } else if (((number / 10) - (number % 10 * 2)) % 7 == 0) {
                System.out.println("It is a Buzz number.");
            }
            else {  // not a Buzz
                System.out.println("It is not a Buzz number.");
                System.out.println("Explanation:");
                System.out.println(number + " is neither divisible by 7 nor does it end with 7");
            }
        } else if (number > 0 && number % 2 == 0) {
            System.out.println("This number is Even.");
            if (number % 7 == 0) {
                System.out.println("It is a Buzz number.");
                System.out.println("Explanation:");
                System.out.println(number + " is divisible by 7");
            } else {
                  System.out.println("It is not a Buzz number.");
                System.out.println("Explanation:");
                System.out.println(number + " is neither divisible by 7 nor does it end with 7");
            }
        } else {
            System.out.println("This number is not natural!");
        }
    }
}
