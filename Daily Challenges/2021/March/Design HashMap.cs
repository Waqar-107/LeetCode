public class MyHashMap {
    public int[] hashmap;
    
    /** Initialize your data structure here. */
    public MyHashMap() {
        hashmap = new int[1000001];
        for(int i = 0; i < 1000001; i++) {
            hashmap[i] = -1;
        }
    }
    
    /** value will always be non-negative. */
    public void Put(int key, int value) {
        hashmap[key] = value;
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int Get(int key) {
        return hashmap[key];
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void Remove(int key) {
        hashmap[key] = -1;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.Put(key,value);
 * int param_2 = obj.Get(key);
 * obj.Remove(key);
 */
