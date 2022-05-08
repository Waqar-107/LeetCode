class MyStack {
public:
    queue<int> q;
    
    MyStack() {
        
    }
    
    void push(int x) {
        q.push(x);
        int sz = q.size();
        
        while(sz > 1) {
            q.push(q.front());
            q.pop();
            sz--;
        }
    }
    
    int pop() {
        int ret = q.front();
        q.pop();
        
        return ret;
    }
    
    int top() {
        return q.front(); 
    }
    
    bool empty() {
        return q.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */