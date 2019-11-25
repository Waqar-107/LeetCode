class MinStack {
public:
    /** initialize your data structure here. */
    stack<int> stk;
    stack<int> mn;
    
    MinStack() {
        
    }
    
    void push(int x) {
        stk.push(x);
        
        if(mn.empty())
            mn.push(x);
        else if(mn.top() >= x)
            mn.push(x);
    }
    
    void pop() {
        if(stk.top() == mn.top())
            mn.pop();
        stk.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return mn.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
