#include <iostream>
#include <queue>
using namespace std;

class Stack {
    queue<int> Q1, Q2;

public:
    Stack() {}

    int getSize() {
        return Q1.size();
    }

    bool isEmpty() {
        return getSize() == 0;
    }

    void push(int element) {
        Q2.push(element);
        while (!Q1.empty()) {
            Q2.push(Q1.front());
            Q1.pop();
        }
        swap(Q1, Q2);
    }

    int pop() {
        if (isEmpty()) return -1;

        int x = Q1.front();
        Q1.pop();
        return x;
    }

    int top() {
        if (isEmpty()) return -1;
        return Q1.front();
    }
};

int main() {
    Stack s;
    s.push(10);
    s.push(20);
    s.push(30);

    cout << "Top element: " << s.top() << endl; 
    cout << "Stack size: " << s.getSize() << endl; 

    cout << "Popped element: " << s.pop() << endl;
    cout << "Top element after pop: " << s.top() << endl; 
    cout << "Stack size after pop: " << s.getSize() << endl; 

    return 0;
}