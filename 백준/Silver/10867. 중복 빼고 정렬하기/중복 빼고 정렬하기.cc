/**
 *    author:  riroan
 *    created:  2024.03.17 20:27:48
 **/
#include <bits/stdc++.h>
#define endl '\n'
#define int long long
using namespace std;

struct Node
{
	Node *l, *r, *p;
	int key;
	Node(int key)
		: key(key)
	{
		l = nullptr;
		r = nullptr;
		p = nullptr;
	}

	bool is_root()
	{
		return p == nullptr;
	}
};

struct SplayTree
{
	Node *root;
	SplayTree()
	{
		root = nullptr;
	}

	void rotate(Node *x)
	{
		// x가 루트
		if (x->is_root())
			return;

		Node *p = x->p;
		Node *r = x->r;
		Node *l = x->l;

		// x가 부모의 왼쪽 자식
		if (p->l == x)
		{
			p->l = r;
			x->r = p;
			if (r)
				r->p = p;
		}

		// x가 부모의 오른쪽 자식
		if (p->r == x)
		{
			p->r = l;
			x->l = p;
			if (l)
				l->p = p;
		}

		x->p = p->p;
		p->p = x;

		// 부모의 부모
		if (x->is_root())
			root = x;
		else
		{
			if (x->p->l == p)
				x->p->l = x;
			else
				x->p->r = x;
		}
	}

	void splay(Node *x)
	{
		while (!x->is_root())
		{
			Node *p = x->p;
			if (x->p->is_root())
			{
				rotate(x);
				return;
			}
			Node *g = p->p;
			if (g->l == p && p->l == x || g->r == p && p->r == x)
			{
				rotate(p);
				rotate(x);
			}
			else
			{
				rotate(x);
			}
		}
	}

	void insert(int key)
	{
		Node *p = root;
		Node *x = new Node(key);
		if (!p)
		{
			root = x;
			return;
		}

		while (1)
		{
			int value = p->key;
			if (value == key)
				return;
			if (value > key)
			{
				if (!p->l)
				{
					p->l = x;
					x->p = p;
					splay(x);
					return;
				}
				p = p->l;
			}
			else
			{
				if (!p->r)
				{
					p->r = x;
					x->p = p;
					splay(x);
					return;
				}
				p = p->r;
			}
		}
	}

	bool contains(int key)
	{
		Node *x = root;
		while (x)
		{
			int value = x->key;
			if (value == key)
			{
				splay(x);
				return true;
			}
			else if (value > key)
				x = x->l;
			else
				x = x->r;
		}
		return false;
	}

	void dfs(Node *x)
	{
		if (x->l)
			dfs(x->l);
		cout << x->key << " ";
		if (x->r)
			dfs(x->r);
	}

	// bool erase(int key)
	// {
	// 	Node *x = root;
	// 	while (x)
	// 	{
	// 		int value = x->key;
	// 		if (value == key)
	// 		{

	// 			return;
	// 		}
	// 		else if (value > key)
	// 			x = x->l;
	// 		else
	// 			x = x->r;
	// 	}
	// }
};

signed main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	SplayTree st;
	int n;
	cin >> n;
	while (n--)
	{
		int x;
		cin >> x;
		st.insert(x);
	}
	st.dfs(st.root);

	return 0;
}
