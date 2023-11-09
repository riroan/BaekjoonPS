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
	vector<int> arr(n);
	for (auto &i : arr)
		cin >> i;
	vector<vector<pair<int, int>>> g(n + 1);
	for (int i = 0; i < n; i++)
	{
		int dx = min(3LL, n - i);
		g[i].push_back({i + 1, arr[i]});
		int s = 0;
		for (int j = 0; j < dx; j++)
			s += arr[i+j];
		g[i].push_back({i + dx, s * 2});
	}
	int inf = -123456789987654321LL;
	vector<int> dp(n + 1, inf);
	for (int i = 0; i < n; i++)
		for (auto [x, y] : g[i])
		{
			if (dp[i] == inf)
				dp[x] = max(dp[x], y);
			else
				dp[x] = max(dp[x], dp[i] + y);
		}
	cout << dp[n] << endl;

	return oOvOo;
}
