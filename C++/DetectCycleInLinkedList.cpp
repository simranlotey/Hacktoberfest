#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

class LinkedList {
public:
    Node* head;
    LinkedList() : head(nullptr) {}

    // Function to add a new node at the end
    void append(int data) {
        Node* newNode = new Node(data);
        if (!head) {
            head = newNode;
            return;
        }
        Node* temp = head;
        while (temp->next) {
            temp = temp->next;
        }
        temp->next = newNode;
    }

    // Function to detect a cycle in the linked list
    bool detectCycle() {
        Node *slow = head, *fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }

    // Function to create a cycle for testing
    void createCycle(int pos) {
        if (pos < 0) return;
        Node* temp = head;
        Node* cycleNode = nullptr;
        int count = 0;

        while (temp->next) {
            if (count == pos) {
                cycleNode = temp;
            }
            temp = temp->next;
            count++;
        }
        if (cycleNode) {
            temp->next = cycleNode;
        }
    }
};

int main() {
    LinkedList list;
    list.append(1);
    list.append(2);
    list.append(3);
    list.append(4);
    list.append(5);

    // Create a cycle for testing (node at position 2 connects back to node 1)
    list.createCycle(1);

    if (list.detectCycle()) {
        cout << "Cycle detected in the linked list." << endl;
    } else {
        cout << "No cycle detected in the linked list." << endl;
    }

    return 0;
}
