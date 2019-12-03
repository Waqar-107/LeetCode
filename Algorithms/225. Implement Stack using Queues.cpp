/***from dust i have come, dust i will be***/

// using a deque

class MyStack {
public:
    deque<int> dq;
    /** Initialize your data structure here. */
    MyStack() {
        
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        dq.push_front(x);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int ret = dq.front();
        dq.pop_front();
        
        return ret;
    }
    
    /** Get the top element. */
    int top() {
        return dq.front();
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return (dq.size() == 0);
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
