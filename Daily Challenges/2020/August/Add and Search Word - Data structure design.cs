public class TrieNode
{
    public bool end;
    public TrieNode[] alpha = new TrieNode[26];

    public TrieNode() {
        end = false;
    }
}

public class WordDictionary
{
    TrieNode root;

    public WordDictionary()
    {
        root = new TrieNode();
    }

    private void addUtil(TrieNode head, string word, int idx)
    {
        if (head.alpha[word[idx] - 'a'] == null) head.alpha[word[idx] - 'a'] = new TrieNode();

        if (idx == word.Length - 1)
        {
            head.alpha[word[idx] - 'a'].end = true;
            return;
        }

        addUtil(head.alpha[word[idx] - 'a'], word, idx + 1);
    }

    public void AddWord(string word)
    {
        addUtil(root, word, 0);
    }

    public bool searchUtil(TrieNode head, string word, int idx)
    {
        if(word.Length - 1 == idx)
        {
            if (word[idx] == '.')
            {
                for(int i = 0; i < 26; i++)
                {
                    if (head.alpha[i] != null && head.alpha[i].end) 
                        return true;
                }

                return false;
            }
            
            else if (head.alpha[word[idx] - 'a'] != null && head.alpha[word[idx] - 'a'].end) return true;
            return false;
        }

        bool flag = false;
        if(word[idx] == '.')
        {
            for(int i = 0; i < 26; i++)
            {
                if (head.alpha[i] != null)
                    flag |= searchUtil(head.alpha[i], word, idx + 1);
            }
        }

        else
        {
            if (head.alpha[word[idx] - 'a'] != null)
                flag = searchUtil(head.alpha[word[idx] - 'a'], word, idx + 1);
        }

        return flag;
    }

    public bool Search(string word)
    {
        return searchUtil(root, word, 0);
    }
}


/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.AddWord(word);
 * bool param_2 = obj.Search(word);
 */
