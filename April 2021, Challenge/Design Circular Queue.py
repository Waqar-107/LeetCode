public class MyCircularQueue
{
    int first, last, sz;
    int[] arr;

    public MyCircularQueue(int k)
    {
        arr = new int[k];
        first = 0;
        last = -1;
        sz = 0;
    }

    public bool EnQueue(int value)
    {
        if (IsFull()) return false;

        last++;
        last %= arr.Length;
        arr[last] = value;
        
        sz++;

        return true;
    }

    public bool DeQueue()
    {
        if (IsEmpty()) return false;

        first++;
        sz--;
        first %= arr.Length;

        return true;
    }

    public int Front()
    {
        if (IsEmpty()) return -1;
        return arr[first];
    }

    public int Rear()
    {
        if (IsEmpty()) return -1;
        return arr[last];
    }

    public bool IsEmpty()
    {
        return sz == 0;
    }

    public bool IsFull()
    {
        return arr.Length == sz;
    }
}
