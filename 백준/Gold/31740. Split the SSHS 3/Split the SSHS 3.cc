/**
 *    author:  riroan
 *    created:  2024.04.07 11:12:04
 **/
#include <bits/stdc++.h>
#define endl '\n'
#define int long long
using namespace std;

signed main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<vector<int>> arr(n);
    vector<int> brr(n);
    for (int i = 0; i < n - 1; i++)
    {
        int a, b;
        cin >> a >> b;
        arr[--a].push_back(--b);
        arr[b].push_back(a);
    }
    for (auto &i : brr)
        cin >> i;
    int s = accumulate(brr.begin(), brr.end(), 0LL);
    int mi = 123456789987654321LL, a = -1, b = -1;
    auto dfs = [&](auto self, int x, int p) -> void
    {
        for (auto i : arr[x])
        {
            if (i == p)
                continue;
            self(self, i, x);
            brr[x] += brr[i];
        }
        int other = s - brr[x], diff = abs(other - brr[x]);
        if (diff <= mi)
        {
            mi = diff;
            a = x + 1;
            b = p + 1;
        }
    };
    dfs(dfs, 0, 0);
    cout << mi << endl;
    cout << a << " " << b << endl;

    return 0;
}
