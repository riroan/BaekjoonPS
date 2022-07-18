#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
const int oOvOo = 0;
using ll = long long;
using namespace std;
constexpr int N = 5000010;
int n;
ll t[2 * N];

ll func(ll a, ll b)
{
    return min(a, b);
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
    ll resl = numeric_limits<ll>::max(), resr = numeric_limits<ll>::max();
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
    int l;
    cin >> n >> l;
    for (int i = 0; i < 2 * N; i++)
        t[i] = 1e9 + 10;
    for (int i = 0; i < n; i++)
        cin >> t[i + n];
    build();
    for (int i = 0; i < n; i++)
        cout << query(max(0, i - l + 1), min(n, i + 1)) << " ";
    return oOvOo;
}