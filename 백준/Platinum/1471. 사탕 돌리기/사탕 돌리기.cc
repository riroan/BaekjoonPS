/**
 *    author:  riroan
 *    created:  2023.11.27 10:20:51
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
#define MAX 200200

signed main()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);
	int n;
	cin >> n;
	int id = 0;
	vector<int> d(n + 1);
	vector<int> finished(n + 1);
	vector<vector<int>> g(n + 1);
	vector<vector<int>> scc;
	stack<int> s;
	auto dfs = [&](auto self, int x) -> int
	{
		d[x] = ++id;
		s.push(x);

		int parent = d[x];
		for (int i = 0; i < g[x].size(); i++)
		{
			int y = g[x][i];
			if (d[y] == 0)
				parent = min(parent, self(self, y));
			else if (!finished[y])
				parent = min(parent, d[y]);
		}
		if (parent == d[x])
		{
			vector<int> sscc;
			while (1)
			{
				int t = s.top();
				s.pop();
				sscc.push_back(t);
				finished[t] = true;
				if (t == x)
					break;
			}
			scc.push_back(sscc);
		}
		return parent;
	};
	for (int i = 0; i < n;i++){
		int t = i+1;
		int r = 0;
		while (t){
			r += t % 10;
			t /= 10;
		}
		int dst = (i + r) % n + 1;
		g[i+1].push_back(dst);
	}
	for (int i = 1; i <= n; i++)
		if (d[i] == 0)
			dfs(dfs, i);
	int size = scc.size();
	vector<int> iscc(n + 1);
	for (int i = 0; i < size; i++)
		for (auto j : scc[i])
			iscc[j] = i;

	vector<vector<pair<int, int>>> brr(size);
	for (int i = 1; i <= n; i++)
		for (auto j : g[i])
		{
			if (iscc[j] != iscc[i])
				brr[iscc[i]].push_back({iscc[j], scc[iscc[j]].size()});
		}
	vector<int> vv(size);
	for (int i = 0; i < size; i++)
		for (auto j : scc[i])
			vv[i] += 0;
	vector<pair<int, int>> dp(size);
	auto dfs2 = [&](auto self, int x) -> pair<int, int>
	{
		if (dp[x].first != 0 && dp[x].second != 0)
			return dp[x];
		int a = scc[x].size();
		int b = vv[x];
		int ma = 0, mb = 1 << 30;
		for (auto [xx, yy] : brr[x])
		{
			auto [aa, bb] = self(self, xx);
			if (aa > ma)
			{
				ma = aa;
				mb = bb;
			}
			else if (aa == ma && bb < mb)
			{
				ma = aa;
				mb = bb;
			}
		}

		if (ma != 0)
			dp[x] = {a + ma, b + mb};
		else
			dp[x] = {a, b};
		return dp[x];
	};
	vector<int> start, ind(size);
	for (auto i : brr)
		for (auto j : i)
			ind[j.first]++;
	for (auto i = 0; i < size; i++)
		if (ind[i] == 0)
			start.push_back(i);
	for (auto i : start)
	{
		dfs2(dfs2, i);
	}
	int ma = 0, mb = 1 << 30;
	for (auto [x, y] : dp)
	{
		if (ma < x)
		{
			ma = x;
			mb = y;
		}
		else if (ma == x && y < mb)
		{
			ma = x;
			mb = y;
		}
	}

	cout << ma << endl;
	return oOvOo;
}
