/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool IsInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     int GetInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     IList<NestedInteger> GetList();
 * }
 */
public class NestedIterator {
    Queue<int> result;
    public NestedIterator(IList<NestedInteger> nestedList) {
        result = new Queue<int>();
        Solve(nestedList);
    }

    public bool HasNext() {
        return result.Count > 0;
    }

    public int Next() {
        return result.Dequeue();
    }
    
    public void Solve(IList<NestedInteger> nestedList)
    {
        foreach(var l in nestedList)
        {
            if(l.IsInteger())
            {
                result.Enqueue(l.GetInteger());
            }   
            else
            {
                Solve(l.GetList());
            }
        }
    }
}

/**
 * Your NestedIterator will be called like this:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.HasNext()) v[f()] = i.Next();
 */
