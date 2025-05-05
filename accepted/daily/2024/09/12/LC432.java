class AllOne {
    
    class Node {
        int cnt;
        Set<String> set;
        Node left, right;
        
        public Node(int cnt) {
            this.cnt = cnt;
            set = new HashSet<>();
        }
    }
    
    Node head, tail;
    Map<String, Node> map;
    public AllOne() {
        head = new Node(-1000);
        tail = new Node(-1000);
        head.right = tail;
        tail.left = head;
        map = new HashMap<>();
    }
    
    private void clear(Node node) {
        if (node.set.isEmpty()) {
            node.left.right = node.right;
            node.right.left = node.left;
        }
    }
    
    private Node insert(Node node, Node insertNode) {
        insertNode.left = node;
        insertNode.right = node.right;
        node.right.left = insertNode;
        node.right = insertNode;
        return insertNode;
    }
    
    public void inc(String key) {
        if (map.containsKey(key)) {
            Node node = map.get(key);
            node.set.remove(key);
            int cnt = node.cnt;
            Node next;
            if (node.right.cnt == cnt + 1) {
                next = node.right;
            } else {
                next = insert(node, new Node(cnt + 1));
            }
            next.set.add(key);
            map.put(key, next);
            clear(node);
        } else {
            Node node;
            if (head.right.cnt == 1) {
                node = head.right;
            } else {
                node = insert(head, new Node(1));
            }
            node.set.add(key);
            map.put(key, node);
        }
    }
    
    public void dec(String key) {
        Node node = map.get(key);
        node.set.remove(key);
        int cnt = node.cnt;
        if (cnt == 1) {
            map.remove(key);
        } else {
            Node pre;
            if (node.left.cnt == cnt - 1) {
                pre = node.left;
            } else {
                pre = insert(node.left, new Node(cnt - 1));
            }
            pre.set.add(key);
            map.put(key, pre);
        }
        clear(node);
    }
    
    public String getMaxKey() {
        Node node = tail.left;
        for (String key : node.set) {
            return key;
        }
        return "";
    }
    
    public String getMinKey() {
        Node node = head.right;
        for (String key : node.set) {
            return key;
        }
        return "";
    }
}

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = new AllOne();
 * obj.inc(key);
 * obj.dec(key);
 * String param_3 = obj.getMaxKey();
 * String param_4 = obj.getMinKey();
 */