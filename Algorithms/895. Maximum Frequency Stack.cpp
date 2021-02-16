struct Node{
    int value, cnt, index;
    Node(int value, int cnt, int index) {
        this->value = value;
        this->cnt = cnt;
        this->index = index;
    }
};

class cmp
{
public:
    bool operator() (Node a, Node b)
    {
        if(a.cnt == b.cnt)
            return a.index < b.index;
        
        return a.cnt < b.cnt;
    }
};


class FreqStack {
public:
    priority_queue<Node, vector<Node>, cmp> pq;
    int total;
    unordered_map<int, int> cnt;
    
    FreqStack() {
        total = 0;
    }
    
    void push(int x) {
        cnt[x]++;
        total++;
        
        pq.push(Node(x, cnt[x], total));
    }
    
    int pop() {
        int ans = pq.top().value;
        pq.pop();
        
        cnt[ans]--;

        return ans;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 */
