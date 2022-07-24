#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
const int oOvOo = 0;
using ll = long long;
using namespace std;
class DisjointSet
{
public:
    vector<int> p;
    int n;
    DisjointSet(int _n) : n(_n)
    {
        p.resize(n);
        iota(p.begin(), p.end(), 0);
    }

    inline int get(int x)
    {
        return (x == p[x] ? x : (p[x] = get(p[x])));
    }

    inline bool unite(int x, int y)
    {
        x = get(x);
        y = get(y);
        if (x != y)
        {
            p[x] = y;
            return true;
        }
        return false;
    }
};
int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    DisjointSet ds(n);
    vector<vector<int>> g(n);
    bool ok = true;
    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        if(ds.get(a) == ds.get(b))
            ok = false;
        else{
            if(g[a].size())
                for(auto i : g[a])
                    ds.unite(i, b);
            else
                g[a].push_back(b);
            if (g[b].size())
                for(auto i :g[b])
                    ds.unite(i, a);
            else
                g[b].push_back(a);
        }
    }
    cout << int(ok) << endl;
    return oOvOo;
}