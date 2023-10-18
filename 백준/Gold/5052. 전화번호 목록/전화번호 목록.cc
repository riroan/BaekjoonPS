#include <iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cstdbool>
#include<cmath>
#include<string>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<sstream>
using namespace std;
#pragma warning(disable:4996)

const int maxChild = 10;
int toNumber(char ch) { return ch - '0'; }

struct trie
{
	trie* children[maxChild];
	bool terminal;
	int numChild;
	trie() : terminal(false)
	{
		memset(children, 0, sizeof(children));
		numChild = 0;
	}
	~trie()
	{
		for (int i = 0; i < maxChild; i++)
			if (children[i])
				delete children[i];
	}

	void insert(const char* key)
	{
		if (*key == 0)
			terminal = true;
		else
		{
			if (terminal)
				terminal = false;
			int next = toNumber(*key);
			if (children[next] == NULL)
				children[next] = new trie();
			children[next]->insert(key + 1);
			numChild++;
		}
	}

	trie* find(const char* key)
	{
		if (*key == 0)
			return this;
		int next = toNumber(*key);
		if (children[next] == NULL) return NULL;
		return children[next]->find(key + 1);
	}
};


int main()
{
	int T;
	scanf("%d", &T);
	while (T--)
	{
		int n;
		scanf("%d", &n);
		trie* tt = new trie;
		char** str = new char*[n];
		for (int i = 0; i < n; i++)
		{
			str[i] = new char[11];
			scanf("%s", str[i]);
			tt->insert(str[i]);
		}
		bool consist = true;
		for (int i = 0; i < n; i++)
		{
			trie* temp = tt->find(str[i]);
			if (temp->numChild)
			{
				consist = false;
				break;
			}
		}
		printf("%s\n", consist ? "YES" : "NO");
	}
}