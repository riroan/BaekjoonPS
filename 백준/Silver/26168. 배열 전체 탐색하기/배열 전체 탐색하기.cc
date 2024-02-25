/**
 *    author:  riroan
 *    created:  2024.02.25 10:08:16
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
	int n, q;
	cin >> n >> q;
	vector<int> arr(n);
	for (auto &i : arr)
		cin >> i;
	ranges::sort(arr);
	while (q--)
	{
		int op;
		cin >> op;
		if (op == 1)
		{
			int k;
			cin >> k;
			auto point = ranges::partition_point(
							 arr, [&](int x)
							 { return x < k; }) -
						 arr.begin();
			cout << n - point << endl;
		}
		else if (op == 2)
		{
			int k;
			cin >> k;
			auto point = ranges::partition_point(
							 arr, [&](int x)
							 { return x <= k; }) -
						 arr.begin();
			cout << n - point << endl;
		}
		else
		{
			int l, r;
			cin >> l >> r;
			auto left = ranges::partition_point(
							arr, [&](int x)
							{ return x < l; }) -
						arr.begin();
			auto right = ranges::partition_point(
							 arr, [&](int x)
							 { return x <= r; }) -
						 arr.begin();
			cout << right - left << endl;
		}
	}
	return oOvOo;
}
