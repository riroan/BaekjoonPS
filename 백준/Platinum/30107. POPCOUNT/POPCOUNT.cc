/**
 *    author:  riroan
 *    created:  2023.10.08 13:52:46
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
	int test;
	cin >> test;
	int cur = 1;
	vector<pair<int, int>> arr;
	for (int i = 1; i <= 500000; i++)
	{
		if (cur * 2 - 1 == i)
			cur *= 2;
		arr.push_back({__builtin_popcountll(cur - 1), __builtin_popcountll(i - cur + 1)});
	}
	vector<int> ps(1), pps(1);
	int c = 0;
	for (auto [x, y] : arr)
	{
		ps.push_back(ps.back() + x);
		pps.push_back(pps.back() + y);
	}
	for (int tc = 1; tc <= test; ++tc)
	{
		int n, a, b;
		cin >> n >> a >> b;
		if (a < b)
			swap(a, b);
		cout << ps[n] * a + pps[n] * b << endl;
	}
	return oOvOo;
}
