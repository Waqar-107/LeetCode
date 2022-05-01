struct Node{
    int value, index, frequency;
    Node(){}
    Node(int value, int frequency, int index){
        this->value = value;
        this->frequency = frequency;
        this->index = index;
    }
};

class cmp
{
public:
    bool operator() (Node a, Node b)
    {
        if(a.frequency == b.frequency) return a.index < b.index;
        return a.frequency < b.frequency;
    }
};

class FreqStack {
public:
    priority_queue<Node, vector<Node>, cmp> pq;
    int idx;
    unordered_map<int, int> cnt;
    
    FreqStack() {
        idx = 0;
    }
    
    void push(int x) {
        cnt[x]++;
        pq.push(Node(x, cnt[x], idx));
        idx++;
    }
    
    int pop() {
        Node u = pq.top();
        cnt[u.value]--;
        pq.pop();
        
        return u.value;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 */
