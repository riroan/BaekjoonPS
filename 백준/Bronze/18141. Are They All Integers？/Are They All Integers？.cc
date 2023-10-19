/**
 *    author:  riroan
 *    created:  2023.10.19 22:20:12
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
	vector<int> arr(n);
	for (auto &i : arr)
		cin >> i;
	bool ok = 1;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < n; k++)
			{
				if (i == j || j == k || k == i)
					continue;
				if ((arr[i] - arr[j]) % arr[k])
					ok = 0;
			}
		}
	}
	if (ok)
		cout << "yes";
	else
		cout << "no";
	return oOvOo;
}
