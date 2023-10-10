#include <iostream>

// Linked List Node Structure
struct Node {
    int data;
    Node* next;

    Node(int value) : data(value), next(nullptr) {}
};

// Function to add a new node at the end of the linked list
void appendNode(Node*& head, int value) {
    Node* newNode = new Node(value);

    if (head == nullptr) {
        // If the list is empty, set the new node as the head
        head = newNode;
    } else {
        // Traverse to the end of the list and add the new node
        Node* current = head;
        while (current->next != nullptr) {
            current = current->next;
        }
        current->next = newNode;
    }
}

// Function to add a new node at the beginning of the linked list
void prependNode(Node*& head, int value) {
    Node* newNode = new Node(value);
    newNode->next = head;
    head = newNode;
}

// Function to add a new node at a specific position in the linked list
void insertNodeAtPosition(Node*& head, int value, int position) {
    Node* newNode = new Node(value);

    if (position == 0 || head == nullptr) {
        // If position is 0 or the list is empty, insert at the beginning
        newNode->next = head;
        head = newNode;
    } else {
        // Traverse to the position and insert the new node
        Node* current = head;
        for (int i = 0; i < position - 1 && current->next != nullptr; ++i) {
            current = current->next;
        }
        newNode->next = current->next;
        current->next = newNode;
    }
}

// Function to delete a node with a given value from the linked list
void deleteNode(Node*& head, int value) {
    if (head == nullptr) {
        std::cout << "List is empty. Nothing to delete." << std::endl;
        return;
    }

    if (head->data == value) {
        // If the value is in the head node, delete the head
        Node* temp = head;
        head = head->next;
        delete temp;
        std::cout << "Node with value " << value << " deleted." << std::endl;
        return;
    }

    // Traverse the list to find the node to delete
    Node* current = head;
    while (current->next != nullptr && current->next->data != value) {
        current = current->next;
    }

    if (current->next != nullptr) {
        // Node with the value found, delete it
        Node* temp = current->next;
        current->next = current->next->next;
        delete temp;
        std::cout << "Node with value " << value << " deleted." << std::endl;
    } else {
        std::cout << "Node with value " << value << " not found." << std::endl;
    }
}

// Function to delete the entire linked list
void deleteList(Node*& head) {
    while (head != nullptr) {
        Node* temp = head;
        head = head->next;
        delete temp;
    }
    std::cout << "List deleted." << std::endl;
}

// Function to print the linked list
void printList(const Node* head) {
    const Node* current = head;
    while (current != nullptr) {
        std::cout << current->data << " ";
        current = current->next;
    }
    std::cout << std::endl;
}

int main() {
    Node* head = nullptr;
    int choice, value, position;

    do {
        // Display menu
        std::cout << "\n----- Menu -----" << std::endl;
        std::cout << "1. Append Node" << std::endl;
        std::cout << "2. Prepend Node" << std::endl;
        std::cout << "3. Insert Node at Position" << std::endl;
        std::cout << "4. Delete Node" << std::endl;
        std::cout << "5. Print List" << std::endl;
        std::cout << "6. Delete Entire List" << std::endl;
        std::cout << "7. Exit" << std::endl;
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                std::cout << "Enter value to append: ";
                std::cin >> value;
                appendNode(head, value);
                break;

            case 2:
                std::cout << "Enter value to prepend: ";
                std::cin >> value;
                prependNode(head, value);
                break;

            case 3:
                std::cout << "Enter value to insert: ";
                std::cin >> value;
                std::cout << "Enter position to insert at: ";
                std::cin >> position;
                insertNodeAtPosition(head, value, position);
                break;

            case 4:
                std::cout << "Enter value to delete: ";
                std::cin >> value;
                deleteNode(head, value);
                break;

            case 5:
                std::cout << "Linked List: ";
                printList(head);
                break;

            case 6:
                deleteList(head);
                break;

            case 7:
                std::cout << "Exiting program." << std::endl;
                break;

            default:
                std::cout << "Invalid choice. Please enter a valid option." << std::endl;
                break;
        }
    } while (choice != 7);

    return 0;
}
