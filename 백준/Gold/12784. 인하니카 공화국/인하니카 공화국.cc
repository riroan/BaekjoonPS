/**
 *    author:  riroan
 *    created:  2024.03.03 13:46:05
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
	int tc;
	cin >> tc;
	while (tc--)
	{
		int n, m;
		cin >> n >> m;
		vector<vector<pair<int, int>>> arr(n);
		while (m--)
		{
			int a, b, c;
			cin >> a >> b >> c;
			a--;
			b--;
			arr[a].emplace_back(b, c);
			arr[b].emplace_back(a, c);
		}
		vector<int> dp(n);
		auto dfs = [&](auto self, int x, int p, int c = 0) -> int
		{
			int s = 0;
			if (arr[x].size() == 1)
				s = c;
			for (auto [i, c] : arr[x])
			{
				if (i == p)
					continue;
				int res = self(self, i, x, c);
				s += min(res, c);
			}
			return s;
		};
		cout << dfs(dfs, 0, 0) << endl;
	}
	return oOvOo;
}
