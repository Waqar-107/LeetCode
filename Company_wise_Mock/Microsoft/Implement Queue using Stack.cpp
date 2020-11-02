class MyQueue {
public:
    stack<int> uno;
    stack<int> dos;
    
    /** Initialize your data structure here. */
    MyQueue() {}
    
    /** Push element x to the back of queue. */
    void push(int x) {
        uno.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if(dos.empty()){
            while(uno.size()){
                dos.push(uno.top());
                uno.pop();
            }
        }
        
        int u = dos.top();
        dos.pop();
        return u;
    }
    
    /** Get the front element. */
    int peek() {
        if(dos.empty()){
            while(uno.size()){
                dos.push(uno.top());
                uno.pop();
            }
        }
        
        int u = dos.top();
        return u;
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return uno.empty() && dos.empty();
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
