#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
const int oOvOo = 0;
using ll = long long;
using namespace std;

constexpr int N = 1000000;
int n;
ll t[2 * N];

ll func(ll a, ll b){
	return a + b;
}

void build()
{
	for (int i = n - 1; i > 0; i--)
		t[i] = func(t[i << 1], t[i << 1 | 1]);
}

void modify(int p, ll v)
{
	for (t[p += n] = v; p > 1; p >>= 1)
		t[p >> 1] = func(t[p], t[p ^ 1]);
}

ll query(int l, int r)
{
	ll resl = 0, resr = 0;
	for (l += n, r += n; l < r; l >>= 1, r >>= 1)
	{
		if (l & 1)
			resl = func(resl, t[l++]);
		if (r & 1)
			resr = func(t[--r], resr);
	}
	return func(resl, resr);
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);
	int m, k;
	cin >> n >> m >> k;
	for (int i = 0; i < n; i++)
		cin >> t[n + i];
	build();
	for (int i = 0; i < m + k; i++)
	{
		ll a, b, c;
		cin >> a >> b >> c;
		if (a == 1)
			modify(b - 1, c);
		else
			cout << query(b - 1, c) << endl;
	}
	return oOvOo;
}