// Define a Node class to represent individual nodes in the linked list.
class Node {
    constructor(data) {
      this.data = data;
      this.next = null;
    }
  }
  
  // Define a LinkedList class to manage the linked list.
  class LinkedList {
    constructor() {
      this.head = null;
      this.tail = null;
    }
  
    // Add a new node to the end of the linked list.
    append(data) {
      const newNode = new Node(data);
  
      if (!this.head) {
        this.head = newNode;
        this.tail = newNode;
      } else {
        this.tail.next = newNode;
        this.tail = newNode;
      }
    }
  
    // Add a new node to the beginning of the linked list.
    prepend(data) {
      const newNode = new Node(data);
  
      if (!this.head) {
        this.head = newNode;
        this.tail = newNode;
      } else {
        newNode.next = this.head;
        this.head = newNode;
      }
    }
  
    // Add a new node at a specific position in the linked list.
    insertAt(position, data) {
      if (position < 0) {
        console.error('Invalid position');
        return;
      }
  
      const newNode = new Node(data);
  
      if (position === 0) {
        this.prepend(data);
      } else {
        let current = this.head;
        let count = 0;
        while (current) {
          if (count === position - 1) {
            newNode.next = current.next;
            current.next = newNode;
            if (!newNode.next) {
              this.tail = newNode;
            }
            return;
          }
          current = current.next;
          count++;
        }
  
        console.error('Position out of range');
      }
    }
  
    // Delete a node with the specified data from the linked list.
    delete(data) {
      if (!this.head) {
        return;
      }
  
      if (this.head.data === data) {
        this.head = this.head.next;
        if (!this.head) {
          this.tail = null;
        }
        return;
      }
  
      let current = this.head;
      while (current.next) {
        if (current.next.data === data) {
          current.next = current.next.next;
          if (!current.next) {
            this.tail = current;
          }
          return;
        }
        current = current.next;
      }
    }
  
    // Delete a node at a specific position in the linked list.
    deleteAt(position) {
      if (position < 0) {
        console.error('Invalid position');
        return;
      }
  
      if (position === 0) {
        this.head = this.head.next;
        if (!this.head) {
          this.tail = null;
        }
        return;
      }
  
      let current = this.head;
      let count = 0;
      while (current.next) {
        if (count === position - 1) {
          current.next = current.next.next;
          if (!current.next) {
            this.tail = current;
          }
          return;
        }
        current = current.next;
        count++;
      }
  
      console.error('Position out of range');
    }
  
    // Search for a node with the specified data in the linked list.
    search(data) {
      let current = this.head;
      while (current) {
        if (current.data === data) {
          return current;
        }
        current = current.next;
      }
      return null;
    }
  
    // Print the elements of the linked list.
    print() {
      const elements = [];
      let current = this.head;
      while (current) {
        elements.push(current.data);
        current = current.next;
      }
      console.log(elements.join(' -> '));
    }
  }
  
  // Example usage:
  const list = new LinkedList();
  
  list.append(1);
  list.append(2);
  list.append(3);
  list.prepend(0);
  list.print();  // Output: 0 -> 1 -> 2 -> 3
  
  list.insertAt(2, 10);
  list.print();  // Output: 0 -> 1 -> 10 -> 2 -> 3
  
  list.deleteAt(1);
  list.print();  // Output: 0 -> 10 -> 2 -> 3
  