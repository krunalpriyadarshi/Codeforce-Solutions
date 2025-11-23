public class LinkedList{
    // Node structure:
    private class Node{
        int data;
        Node next;

        Node(int value){
            this.data = value;
            this.next = null;
        }
    }

    // LinkedList Meta data:
    public int size;
    public Node head;   // First node

    // Constrcutor;
    public LinkedList(){
        this.size = 0;
        this.head = null;
    }

    // Insert
    // Insert node at first index:
    public void addFirst(int value){
        // If LinkedList is empty:
        if(size == 0)
            head = new Node(value);
        // If LinkedList is non-empty:
        else{
            Node newNode = new Node(value);
            newNode.next = head.next;
            head.next = newNode;
        }
        
        size++;
    }

    // Utilities:
    // Checks if LinkedList is empty:
    public boolean isEmpty(){
        return size == 0;
    }

    // Returns the size of LinkedList:
    public int size(){
        return this.size;
    }

    // Prints LinkedList:
    public void print(){

        if(this.isEmpty()){
            System.out.println("Empty LinkedList");
            return;
        }

        Node curr = head;
        while(curr != null){
            System.out.print(curr.data + " ");
            curr = curr.next;
        }
        System.out.println("");
    }

}