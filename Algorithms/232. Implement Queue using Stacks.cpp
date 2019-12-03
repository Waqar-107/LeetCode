/***from dust i have come, dust i will be***/

class MyQueue {
    stack<int> stk1;
    stack<int> stk2;
public:
    /** Initialize your data structure here. */
    MyQueue() {}
    
    /** Push element x to the back of queue. */
    void push(int x) {
        stk1.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        while(stk1.size() > 1){
            stk2.push(stk1.top());
            stk1.pop();
        }
        
        int ret = stk1.top();
        stk1.pop();
        
        while(stk2.size()){
            stk1.push(stk2.top());
            stk2.pop();
        }
        
        return ret;
    }
    
    /** Get the front element. */
    int peek() {
        while(stk1.size()){
            stk2.push(stk1.top());
            stk1.pop();
        }
        
        int ret = stk2.top();
        
        while(stk2.size()){
            stk1.push(stk2.top());
            stk2.pop();
        }
        
        return ret;
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return (stk1.size() == 0);
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
