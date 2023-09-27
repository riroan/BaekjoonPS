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
    int n, m;
    cin >> n >> m;
    string s;
    cin >> s;
    vector<pair<int, int>> arr;
    int r = 1;
    int start = 0;
    for (int i = 1; i < n; i++)
    {
        if (s[i] == s[i - 1])
            r++;
        else
        {
            arr.push_back({start, r});
            start = i;
            r = 1;
        }
    }
    arr.push_back({start, r});
    vector<int> brr;
    for (auto [x, y] : arr)
        for (int i = 0; i <= y - m; i++)
            brr.push_back(x + i);
    if (brr.size() == 0)
    {
        cout << n << endl;
        return 0;
    }
    sort(brr.begin(), brr.end());
    brr.push_back(1LL << 62);
    int ans = 0;
    // for (auto i : brr)
    //     cout << i << " ";
    // cout << endl;
    for (int i = 1; i <= n; i++)
    {
        bool ok = 1;
        int ma = 0;
        // cout << ">> " << i << endl;
        for (int j = 0; j <= n; j += i)
        {
            vector<int> diff(26);
            int left = j, right = min(j + i, n);
            int l = *lower_bound(brr.begin(), brr.end(), left);
            if (l + m-1 < right)
                ok = 0;
            // cout << left << " " << right << " " << l << " " << ok << endl;
        }
        // cout << i << " " << ma << endl;
        // cout << endl;

        if (ok)
            ans = max(ans, i);
    }
    cout << ans << endl;

    return oOvOo;
}
