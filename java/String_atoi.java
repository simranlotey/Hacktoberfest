import java.util.*;

class String_atoi {
    // Method to convert a string to an integer
    public int myAtoi(String s) {
        int i = 0;              
        int A = 1;             
        int count = 0;          
        long sum = 0;           
        int count1 = 0;         
        int N = s.length();     

        // Skip leading whitespaces
        while (i < N && s.charAt(i) == ' ') {
            i++;
        }

        // Start processing each character in the string from the first non-space
        for (int k = i; k < N; k++) {
            char C = s.charAt(k);  

            // Handle the initial sign and digit checks
            if (count == 0 && count1 == 0) {
                if (C == '-') {
                    A = -1;       
                    count1++;     
                } else if (C == '+') {
                    A = 1;     
                    count1++;  
                } else if (C < '0' || C > '9') {
                    return 0;     // Return 0 if the first non-space character is not a digit or sign
                } else if (C >= '0' && C <= '9') {
                    sum = sum * 10 + (int)(C - '0');  
                    count++;    
                }
            }
            // If a digit has already been processed
            else if (count > 0) {
                if (C == '-' || C == '+') {
                    break;        // Stop if another sign is encountered after initial digits
                } else if (C < '0' || C > '9') {
                    break;        // Stop if a non-digit character is encountered after digits
                } else if (C >= '0' && C <= '9') {
                    sum = sum * 10 + (int)(C - '0');  // Continue building the integer
                    count++;
                }
            }
            // If a sign has already been processed without a digit
            else if (count1 > 0) {
                if (C == '-' || C == '+') {
                    return 0;     
                } else if (C < '0' || C > '9') {
                    return 0;     
                } else if (C >= '0' && C <= '9') {
                    sum = sum * 10 + (int)(C - '0');  // Start calculating sum with first digit
                    count++;
                }
            }

            // Check for integer overflow and handle it
            if (sum * A > Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;  
            } else if (sum * A < Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;  
            }
        }

        return (int) sum * A;  // Return final converted integer after processing all valid characters
    }

    // Main method to run and test the myAtoi function
    public static void main(String[] args) {
        String_atoi converter = new String_atoi();  
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int result = converter.myAtoi(str);        
        System.out.println("The converted integer is: " + result);  
        sc.close();
    }
}
