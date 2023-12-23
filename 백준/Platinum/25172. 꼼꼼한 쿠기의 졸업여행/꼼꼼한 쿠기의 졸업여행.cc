/**
 *    author:  riroan
 *    created:  2023.12.23 22:12:00
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

class DisjointSet
{
public:
    vector<int> f, siz;

    DisjointSet(int n)
    {
        f.resize(n);
        siz.resize(n, 1);
        iota(f.begin(), f.end(), 0);
    }

    int get(int x)
    {
        while (x != f[x])
        {
            f[x] = f[f[x]];
            x = f[x];
        }
        return x;
    }

    void unite(int x, int y)
    {
        x = get(x);
        y = get(y);
        if (x != y)
        {
            siz[x] += siz[y];
            f[y] = x;
        }
    }

    int size(int x)
    {
        return siz[get(x)];
    }
};

signed main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<set<int>> arr(n);
    while (m--)
    {
        int a, b;
        cin >> a >> b;
        arr[--a].insert(--b);
        arr[b].insert(a);
    }
    vector<int> query(n);
    for (auto &i : query)
    {
        cin >> i;
        i--;
    }
    DisjointSet ds(n);
    set<int> s;
    vector<string> ans;
    ans.push_back("DISCONNECT");
    for (int i = 0; i < n; i++)
    {
        int x = query[n - i - 1];
        for (auto j : arr[x])
            if (s.contains(j))
                ds.unite(min(j, x), max(j, x));
        s.insert(x);
        if (ds.size(x) == s.size())
            ans.push_back("CONNECT");
        else
            ans.push_back("DISCONNECT");
    }

    reverse(ans.begin(), ans.end());
    for (auto i : ans)
        cout << i << endl;
    return oOvOo;
}
