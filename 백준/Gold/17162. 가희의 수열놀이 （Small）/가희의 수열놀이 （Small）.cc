/**
 *    author:  riroan
 *    created:  2023.10.28 19:52:33
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
    int q, mod;
    cin >> q >> mod;
    vector<int> arr;
    vector<priority_queue<int>> pq(mod);
    while (q--)
    {
        int op;
        cin >> op;
        if (op == 1)
        {
            int x;
            cin >> x;
            pq[x % mod].push(arr.size());
            arr.push_back(x % mod);
        }
        else if (op == 2)
        {
            if (arr.size())
            {
                int x = arr.back();
                pq[x].pop();
                arr.pop_back();
            }
        }
        else
        {
            int mi = 123456789;
            for (int i = 0; i < mod; i++)
            {
                if (pq[i].empty())
                {
                    mi = arr.size() + 1;
                    break;
                }
                mi = min(mi, pq[i].top());
            }
            cout << (int)arr.size() - mi << endl;
        }
    }
    return oOvOo;
}
