public class MyHashSet {
    public bool[] hash;

    /** Initialize your data structure here. */
    public MyHashSet() {
        hash = new bool[1000001];
        for(int i = 0; i <= 1000000; i++) hash[i] = false;
    }
    
    public void Add(int key) {
        hash[key] = true;
    }
    
    public void Remove(int key) {
        hash[key] = false;
    }
    
    /** Returns true if this set contains the specified element */
    public bool Contains(int key) {
        return hash[key];
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.Add(key);
 * obj.Remove(key);
 * bool param_3 = obj.Contains(key);
 */
