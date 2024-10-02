// Problem: Given a singly linked list, return the middle node of the list. If there are two middle nodes, return the second middle node.

#include<bits/stdc++.h>
#include <iostream>
using namespace std;

// Definition for singly-linked list node
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        // Move `slow` one step at a time and `fast` two steps at a time
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // When `fast` reaches the end, `slow` is at the middle
        return slow;
    }
};

// Helper function to create a linked list
ListNode* createLinkedList(const vector<int>& values) {
    ListNode* head = new ListNode(values[0]);
    ListNode* current = head;
    for (int i = 1; i < values.size(); ++i) {
        current->next = new ListNode(values[i]);
        current = current->next;
    }
    return head;
}

// Helper function to print the linked list from a given node
void printLinkedList(ListNode* node) {
    while (node != nullptr) {
        cout << node->val << " ";
        node = node->next;
    }
    cout << endl;
}

int main() {
    vector<int> values = {1, 2, 3, 4, 5};
    ListNode* head = createLinkedList(values);

    Solution solution;
    ListNode* middle = solution.middleNode(head);

    cout << "Middle of the Linked List: ";
    printLinkedList(middle);  // It will print from the middle node
    return 0;
}
