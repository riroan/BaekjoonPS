#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
const int oOvOo = 0;
using ll = long long;
using namespace std;

constexpr int N = 131072;
int n;
ll t[2 * N];

ll func(ll a, ll b)
{
    return a + b;
}

void build()
{
    for (int i = n - 1; i > 0; i--)
        t[i] = func(t[i << 1], t[i << 1 | 1]);
}

void modify(int p, ll v)
{
    for (t[p += n] += v; p > 1; p >>= 1)
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
    cin >> n;
    vector<ll> arr(n);
    for (auto &i : arr)
        cin >> i;
    vector<ll> minarr(N), maxarr(N);

    for (auto i = 0; i < n; i++)
    {
        modify(arr[i], 1);
        maxarr[i] = query(arr[i] + 1, n + 1);
    }

    reverse(arr.begin(), arr.end());
    for (int i = 0; i < 2 * N; i++)
        t[i] = 0;
    for (auto i = 0; i < n; i++)
    {
        modify(arr[i], 1);
        minarr[n - i - 1] = query(1, arr[i]);
    }
    ll ans = 0;
    for (int i = 0; i < n; i++)
    {
        ans += (minarr[i]) * maxarr[i];
    }
    cout << ans << endl;

    return oOvOo;
}