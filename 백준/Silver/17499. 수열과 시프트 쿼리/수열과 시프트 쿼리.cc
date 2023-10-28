/**
 *    author:  riroan
 *    created:  2023.10.28 15:31:28
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
    int ix = 0;
    while (q--)
    {
        int op;
        cin >> op;
        if (op == 1)
        {
            int a, b;
            cin >> a >> b;
            arr[(ix + a - 1) % n] += b;
        }
        else if (op == 3)
        {
            int x;
            cin >> x;
            ix += x;
            ix %= n;
        }
        else
        {
            int x;
            cin >> x;
            ix -= x;
            if (ix < 0)
                ix += n;
        }
    }
    for (int i = 0; i < n; i++)
        cout << arr[(i + ix) % n] << " ";
    return oOvOo;
}
