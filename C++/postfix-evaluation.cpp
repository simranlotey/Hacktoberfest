#include <iostream>
#include <stack>
#include <string>
#include <cctype>

// algorithm used:
// 1. initialize stack to store operands
// 2. scan the expression from left to right and do the following for every element
// 3. if the element is an operand, push it into the stack
// 4. if the element is an operator, pop two operands from the stack and apply the operator, push the result back into the stack
// 5. when the expression is ended, the number in the stack is the final result


int evalPostfix(std::string exp) {
    std::stack<int> stack;
    for (char c : exp) {
        if (isdigit(c)) {
            stack.push(c - '0');
        } else {
            int a = stack.top();
            stack.pop();
            int b = stack.top();
            stack.pop();
            switch (c) {
                case '+':
                    stack.push(b + a);
                    break;
                case '-':
                    stack.push(b - a);
                    break;
                case '*':
                    stack.push(b * a);
                    break;
                case '/':
                    stack.push(b / a);
                    break;
            }
        }
    }
    return stack.top();
}

int main() {
    std::string expression = "231*+9-";  // Example postfix expression

    int result = evalPostfix(expression);
    std::cout << "The result of the postfix expression is: " << result << std::endl;

    return 0;

}
