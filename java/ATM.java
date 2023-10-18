import java.util.*;
import java.util.Scanner;

public class ATM{
    public static void main(String args[]) {
        int debit = 10000;
        int credit = 10000;
        int balance = 10000;
        balance = 100000;
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("Select option 1 for debit");
            System.out.println("Select option 2 for credit");
            System.out.println("Select option 3 for balance");
            System.out.println("Select option 4 for exit");
            System.out.println("Select an option : ");
            int s = sc.nextInt();
            switch(s)
            {
                case 1:
                    System.out.println("amount:");
                    debit = sc.nextInt();
                    if(debit<=balance)
                    {
                        balance = balance-debit;
                        System.out.println("Amount debited succesfully.");
                    }
                    else
                    {
                        System.out.println("in sufficient balance");
                    }
                    System.out.println("\nBalance is : "+balance);
                    break;
                case 2:
                    System.out.println("\nEnter amount to be credited : ");
                    credit= sc.nextInt();
                    balance = balance+credit;
                    System.out.println("\nAmount credited succesfully.");
                    System.out.println("Balance is : "+balance);
                    break;

                case 3:
                    System.out.println("\nBalance is :"+ balance);
                    break;

                case 4:
                    System.out.println("Thanks for using our services.");
                    System.exit(0);
            }
        }
    }
}
