#define pb push_back
typedef long long int ll;

//gives answer in 32-bits
string decToBin(int n)
{
	string s = "";
	while (n)
	{
		s.pb(n % 2 + 48);
		n /= 2;
	}

	while (s.length() < 32)
		s.pb('0');

	reverse(s.begin(), s.end());
	return s;
}

int toDecimal(string s)
{
    int sum = 0;
    ll p = 1;
    for(int i = 31; i >=0; i--)
    {
        sum += p * (s[i] - 48);
        p *= 2;
    }

    return sum;
}

struct trieNode
{
	bool end;
	trieNode *next[2];

	trieNode() {
		end = false;
		for (int i = 0; i < 2; i++)
			next[i] = NULL;
	}
};

class trie
{
	trieNode *root;
public:
	trie() {
		root = new trieNode();
	}

	void insertWord(string s)
	{
		trieNode *curr = root;

		int n = s.length(), id;
		for (int i = 0; i < n; i++)
		{
			id = s[i] - '0';

			if (curr->next[id] == NULL)
				curr->next[id] = new trieNode();

			curr = curr->next[id];
		}

		curr->end = true;
	}

	int solve(int n)
	{
	    string s = decToBin(n), ans;

	    trieNode *curr = root;
	    for(int i = 0; i < 32; i++)
        {
            //get 1
            if(s[i] == '0')
            {
                if(curr->next[1] == NULL)
                    ans.pb('0'), curr = curr->next[0];
                else
                    ans.pb('1'), curr = curr->next[1];
            }

            //get 0
            else
            {
                if(curr->next[0] == NULL)
                    ans.pb('1'), curr = curr->next[1];
                else
                    ans.pb('0'), curr = curr->next[0];
            }
        }

        return toDecimal(ans);
	}
};

class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        int mx = 0;
        trie t;
        
        for(int i = 0; i < nums.size(); i++) t.insertWord(decToBin(nums[i]));
        
        for(int i = 0; i < nums.size(); i++)
            mx = max(mx, nums[i] ^ t.solve(nums[i]));
        
        return mx;
    }
};
