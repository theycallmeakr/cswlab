import java.util.Scanner;

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}
class linked {
    Node head;
    public void add(int data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
            return;
        }
        Node temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = newNode;
    }

    public void addHead(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }

    public void display() {
        if (head == null) {
            System.out.println("List is empty");
            return;
        }

        Node temp = head;
        System.out.print("Linked List: ");
        while (temp != null) {
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.println("null");
    }
    
    public void delAny(int loc) {
        if (head == null) {
            System.out.println("List is empty.");
            return;
        }
        if (loc == 1) {
            head = head.next;
            return;
        }
        Node temp = head;
        for (int i = 1; i < loc - 1 && temp != null; i++) {
            temp = temp.next;
        }

        if (temp == null || temp.next == null) {
            System.out.println("Invalid position.");
            return;
        }
        temp.next = temp.next.next;
    }
    public void Any(int lc) {
        Node temp = head;
        for (int i = 1; i < lc - 1 && temp != null; i++) {
            temp = temp.next;
        }

        if (temp == null || temp.next == null) {
            System.out.println("Invalid position.");
            return;
        }
        System.out.println(temp.data);
    }
}

public class Main {
    public static void main(String[] args) {
        linked list = new linked();

        list.add(3);
        list.add(5);
        list.add(6);
        list.add(7);

        list.display();

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter node position to delete: ");
        int pos = sc.nextInt();

        list.delAny(pos);
        System.out.print("Enter node position to search: ");
        int ps = sc.nextInt();

        list.Any(ps);

        list.display();
    }
}
