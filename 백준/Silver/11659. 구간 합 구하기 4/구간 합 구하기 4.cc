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
	int key, cnt, value, sum;
	Node(int key, int value = 0)
		: key(key), cnt(1), value(value), sum(value)
	{
		l = nullptr;
		r = nullptr;
		p = nullptr;
	}

	inline bool is_root()
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

	void update(Node *x)
	{
		x->cnt = 1;
		x->sum = x->value;
		if (x->l)
		{
			x->cnt += x->l->cnt;
			x->sum += x->l->sum;
		}
		if (x->r)
		{
			x->cnt += x->r->cnt;
			x->sum += x->r->sum;
		}
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
		update(p);
		update(x);
	}

	void splay(Node *x, Node *y = nullptr)
	{
		while (x->p != y)
		{
			Node *p = x->p;
			if (p->p == y)
			{
				rotate(x);
				break;
			}
			Node *g = p->p;
			if (g->l == p && p->l == x || g->r == p && p->r == x)
				rotate(p);
			rotate(x);
		}
		if (!y)
			root = x;
	}

	Node *gather(int s, int e)
	{
		find_kth(e+1);
		auto tmp = root;
		find_kth(s - 1);
		splay(tmp, root);
		return root->r->l;
	}

	void insert(int key, int v = 0)
	{
		Node *p = root;
		Node *x = new Node(key, v);
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

	bool find(int key)
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

	void dfs(auto &&func, Node *x = nullptr)
	{
		if (!x)
			x = root;
		if (x->l)
			dfs(func, x->l);
		func(x);
		if (x->r)
			dfs(func, x->r);
	}

	bool erase(int key)
	{
		if (!find(key))
			return false;
		Node *x = root;
		Node *l = x->l, *r = x->r;
		if (l && r)
		{
			root = l;
			Node *x = root;
			while (x->r)
				x = x->r;
			x->r = r;
			r->p = x;
		}
		else if (l)
			root = l;
		else if (r)
			root = r;
		else
			root = nullptr;
		if (root)
			root->p = nullptr;
		delete x;
		return true;
	}

	void find_kth(int k)
	{
		Node *x = root;
		while (1)
		{
			while (x->l && x->l->cnt > k)
				x = x->l;

			if (x->l)
				k -= x->l->cnt;

			if (!k--)
				break;
			x = x->r;
		}
		splay(x);
	}

	inline int get()
	{
		return root->key;
	}
};

signed main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	int n, q;
	cin >> n >> q;
	SplayTree st;
	st.insert(-1);
	for (int i = 0; i < n; i++)
	{
		int x;
		cin >> x;
		st.insert(i, x);
	}
	st.insert(n);

	while (q--)
	{
		int a, b;
		cin >> a >> b;
		cout << st.gather(a, b)->sum << endl;
	}

	return 0;
}
