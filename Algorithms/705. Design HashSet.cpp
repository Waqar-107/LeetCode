#define N 1000001
class MyHashSet {
public:
    /** Initialize your data structure here. */
    bool hashset[N];
    MyHashSet() {
        memset(hashset, false, sizeof(hashset));
    }
    
    void add(int key) {
        hashset[key] = true;
    }
    
    void remove(int key) {
        hashset[key] = false;
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        return hashset[key];
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
