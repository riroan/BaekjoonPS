/**
 *    author:  riroan
 *    created:  2023.12.01 19:56:34
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

struct BCC
{
    int n, cur, cpiv;
    vector<int> dfn, low, par, vis;
    vector<vector<int>> g, bcc;
    BCC(int n)
    {
        this->n = n;
        dfn.resize(n);
        low.resize(n);
        par.resize(n);
        vis.resize(n);
        g.resize(n, {});
        bcc.resize(n, {});
        cur = 0;
        cpiv = 0;
    }

    void add(int a, int b)
    {
        g[a].push_back(b);
        g[b].push_back(a);
    }

    void dfs(int x, int p)
    {
        dfn[x] = low[x] = ++cur;
        par[x] = p;
        for (int i = 0; i < g[x].size(); i++)
        {
            int w = g[x][i];
            if (w == p)
                continue;
            if (!dfn[w])
            {
                dfs(w, x);
                low[x] = min(low[x], low[w]);
            }
            else
                low[x] = min(low[x], dfn[w]);
        }
    }

    void color(int x, int c)
    {
        if (c > 0)
            bcc[x].push_back(c);
        vis[x] = 1;
        for (int i = 0; i < g[x].size(); i++)
        {
            int w = g[x][i];
            if (vis[w])
                continue;
            if (dfn[x] <= low[w])
            {
                bcc[x].push_back(++cpiv);
                color(w, cpiv);
            }
            else
                color(w, c);
        }
    }

    void build()
    {
        for (int i = 0; i < n; i++)
            if (!dfn[i])
                dfs(i, 0);
        for (int i = 0; i < n; i++)
            if (!vis[i])
                color(i, 0);
    }

    auto get_articulation_point()
    {
        vector<int> res;
        for (int i = 0; i < n; i++)
            if (bcc[i].size() > 1)
                res.push_back(i);
        return res;
    }
};

signed main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    BCC bcc(n);
    while (m--)
    {
        int a, b;
        cin >> a >> b;
        bcc.add(--a, --b);
    }
    bcc.build();
    vector<int> ans = bcc.get_articulation_point();
    cout << ans.size() << endl;
    for (auto i : ans)
        cout << i + 1 << " ";
    return oOvOo;
}
