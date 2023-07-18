struct Node {
    int value, key;
    Node *prev, *next;
    Node(){}
    Node(int key, int value) {
        this->key = key;
        this->value = value;
        this->next = NULL;
        this->prev = NULL;
    }
};

class LRUCache {
public:
    unordered_map<int, Node*> hashmap;
    int capacity, sz;
    Node *head, *tail;

    LRUCache(int capacity) {
        this->capacity = capacity;
        this->sz = 0;

        this->head = new Node();
        this->tail = new Node();

        this->head->next = tail;
        this->tail->prev = head;
    }

    Node* removeNode(Node *node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;

        return node;
    }

    void addNodeToHead(Node *node) {
        head->next->prev = node;
        node->next = head->next;
        head->next = node;
        node->prev = head;
    }
    
    int get(int key) {
        if(hashmap.find(key) == hashmap.end()) return -1;

        // The key exists. Move it to the head
        Node *node = hashmap[key];

        removeNode(node);
        addNodeToHead(node);

        return hashmap[key]->value;
    }

    void printList(Node *node) {
        Node *temp = node;
        while(temp != NULL) {
            cout << temp->value << " ";
            temp = temp->next;
        }

        cout << endl;
    }
    
    void put(int key, int value) {
        if(sz >= capacity && hashmap.find(key) == hashmap.end()) {
            hashmap.erase(tail->prev->key);
            Node* rem = removeNode(tail->prev);
            
            delete rem;
        }

        if(hashmap.find(key) != hashmap.end()) {
            hashmap[key]->value = value;
            Node *node = hashmap[key];

            removeNode(node);
            addNodeToHead(node);
        } else {
            Node *newNode = new Node(key, value);
            addNodeToHead(newNode);

            hashmap[key] = newNode;
            sz++;
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
