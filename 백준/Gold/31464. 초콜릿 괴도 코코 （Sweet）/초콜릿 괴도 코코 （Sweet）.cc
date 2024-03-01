/**
 *    author:  riroan
 *    created:  2024.03.01 13:19:23
 **/
#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
#define int long long
const int oOvOo = 0;
using ll = long long;
using namespace std;

struct BCC
{
	int n, cur, cpiv;
	vector<int> dfn, low, par, vis;
	vector<vector<int>> g, bcc, ibcc;
	BCC(int n)
	{
		this->n = n;
		dfn.resize(n);
		low.resize(n);
		par.resize(n);
		vis.resize(n);
		g.resize(n, {});
		bcc.resize(n, {});
		cur = 0;
		cpiv = 0;
	}

	void add(int a, int b)
	{
		g[a].push_back(b);
	}

	int dfs(int x, int p)
	{
		dfn[x] = low[x] = ++cur;
		par[x] = p;
		for (auto w : g[x])
		{
			if (w == p)
				continue;
			if (!dfn[w])
				low[x] = min(low[x], dfs(w, x));
			else
				low[x] = min(low[x], dfn[w]);
		}
		return low[x];
	}
	void color(int x, int c)
	{
		if (c)
			bcc[x].push_back(c);
		vis[x] = 1;
		for (auto w : g[x])
		{
			if (vis[w])
				continue;
			if (dfn[x] <= low[w])
			{
				bcc[x].push_back(++cpiv);
				color(w, cpiv);
			}
			else
				color(w, c);
		}
	}

	void build()
	{
		for (int i = 0; i < n; i++)
			if (!dfn[i])
				dfs(i, 0);
		for (int i = 0; i < n; i++)
			if (!vis[i])
				color(i, 0);
		ibcc.resize(cpiv);
		for (int i = 0; i < n; i++)
			for (auto j : bcc[i])
				ibcc[j - 1].push_back(i);
	}

	auto get_articulation_point()
	{
		vector<int> res;
		for (int i = 0; i < n; i++)
			if (bcc[i].size() > 1)
				res.push_back(i);
		return res;
	}

	auto get_articulation_bridge()
	{
		vector<pair<int, int>> res;
		for (auto i : ibcc)
			if (i.size() == 2)
				res.push_back(minmax(i[0], i[1]));
		sort(res.begin(), res.end());
		return res;
	}
};

signed main()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);
	int n;
	cin >> n;
	vector<string> arr(n);
	for (auto &i : arr)
		cin >> i;
	auto check = [&](int x, int y)
	{
		return 0 <= x && x < n && 0 <= y && y < n;
	};
	BCC bcc(n * n);
	for (int x = 0; x < n; x++)
	{
		for (int y = 0; y < n; y++)
		{
			for (auto [dx, dy] : vector<pair<int, int>>({{-1, 0}, {1, 0}, {0, -1}, {0, 1}}))
			{
				int tx = x + dx, ty = y + dy;
				if (!check(tx, ty))
					continue;
				if (arr[x][y] == '#' && arr[tx][ty] == '#')
				{
					int cur = x * n + y;
					int dst = tx * n + ty;
					bcc.add(cur, dst);
				}
			}
		}
	}
	bcc.build();
	auto tmp = bcc.get_articulation_point();
	set<int> art(tmp.begin(), tmp.end());
	vector<pair<int, int>> ans;
	for (int x = 0; x < n; x++)
	{
		for (int y = 0; y < n; y++)
		{
			if (arr[x][y] == '.')
				continue;
			if (art.contains(x * n + y))
				continue;
			arr[x][y] = '.';
			BCC bcc(n * n);
			for (int x = 0; x < n; x++)
			{
				for (int y = 0; y < n; y++)
				{
					for (auto [dx, dy] : vector<pair<int, int>>({{-1, 0}, {1, 0}, {0, -1}, {0, 1}}))
					{
						int tx = x + dx, ty = y + dy;
						if (!check(tx, ty))
							continue;
						if (arr[x][y] == '#' && arr[tx][ty] == '#')
						{
							int cur = x * n + y;
							int dst = tx * n + ty;
							bcc.add(cur, dst);
						}
					}
				}
			}
			bcc.build();
			auto p = bcc.get_articulation_point();
			set<int> point(p.begin(), p.end());
			bool ok = 1;
			for (int i = 0; i < n * n; i++)
			{
				if (bcc.g[i].size() >= 2 && !point.contains(i)){
					// cout << bcc.g[i].size() << " " << point.contains(i)<<endl;
					ok = 0;
				}
			}
			if (ok)
				ans.push_back({x + 1, y + 1});
			arr[x][y] = '#';
		}
	}
	ranges::sort(ans);
	cout << ans.size() << endl;
	for (auto [x, y] : ans)
		cout << x << " " << y << endl;
	return oOvOo;
}
