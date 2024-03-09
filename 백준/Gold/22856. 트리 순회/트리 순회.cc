/**
 *    author:  riroan
 *    created:  2024.03.09 17:27:40
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

signed main()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);
	int n;
	cin >> n;
	vector<vector<int>> arr(n);
	for (int i = 0; i < n; i++)
	{
		int a, b, c;
		cin >> a >> b >> c;
		a--;
		b--;
		c--;
		arr[a].push_back(b);
		arr[a].push_back(c);
	}
	int last = 0;
	auto get_last = [&](auto self, int x) -> void
	{
		last = x;
		if (arr[x][1] >= 0)
			self(self, arr[x][1]);
	};
	int ans = 0;
	int fin = 0;
	get_last(get_last, 0);
	auto dfs = [&](auto self, int x) -> void
	{
		for (auto i : arr[x])
		{
			if (i >= 0)
			{
				ans++;
				self(self, i);
			}
		}
		if (last == x)
			fin = 1;
		if (!fin)
			ans++;
	};
	dfs(dfs, 0);
	cout << ans << endl;
	return oOvOo;
}
