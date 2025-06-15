class MyLinkedList {
    class Node {
        int val;
        Node next;
        public Node() {}
        public Node(int val , Node next) {
            this.val = val;
            this.next = next;
        }
    }
    
    Node dummy;
    int length;
    
    public MyLinkedList() {
        dummy = new Node();
        length = 0;
    }
    
    public int get(int index) {
        if (index < 0 || index >= length) return -1;
        Node curNode = dummy.next;
        while(index-- > 0) curNode = curNode.next;
        return curNode.val;
    }
    
    public void addAtHead(int val) {
        dummy.next = new Node(val, dummy.next);
        length++;
    }
    
    public void addAtTail(int val) {
        Node curNode = dummy;
        while (curNode.next != null) curNode = curNode.next;
        curNode.next = new Node(val, null);
        length++;
    }
    
    public void addAtIndex(int index, int val) {
        if (index > length) return ;
        else if (index == length) addAtTail(val);
        else if (index <= 0) addAtHead(val);
        else {
            Node curNode = dummy;
            while (index-- > 0) {
                curNode = curNode.next;
            }
            curNode.next = new Node(val, curNode.next);
            length++;
        }
    }
    
    public void deleteAtIndex(int index) {
        if (index < length) {
            Node curNode = dummy;
            while (index-- > 0) curNode = curNode.next;
            curNode.next = curNode.next.next;
            length--;
        }
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */