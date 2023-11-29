/**
 *    author:  riroan
 *    created:  2023.11.29 16:42:09
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

struct SCC
{
    int n;
    std::vector<std::vector<int>> adj;
    std::vector<int> stk;
    std::vector<int> dfn, low, iscc;
    vector<vector<int>> scc;
    int cur, cnt;

    SCC() {}
    SCC(int n)
    {
        init(n);
    }

    void init(int n)
    {
        this->n = n;
        adj.assign(n, {});
        dfn.assign(n, -1);
        low.resize(n);
        iscc.assign(n, -1);
        stk.clear();
        cur = cnt = 0;
    }

    void add(int u, int v)
    {
        adj[u].push_back(v);
    }

    void dfs(int x)
    {
        dfn[x] = low[x] = cur++;
        stk.push_back(x);

        for (auto y : adj[x])
        {
            if (dfn[y] == -1)
            {
                dfs(y);
                low[x] = std::min(low[x], low[y]);
            }
            else if (iscc[y] == -1)
            {
                low[x] = std::min(low[x], dfn[y]);
            }
        }

        if (dfn[x] == low[x])
        {
            int y;
            do
            {
                y = stk.back();
                iscc[y] = cnt;
                stk.pop_back();
            } while (y != x);
            cnt++;
        }
    }

    void build()
    {
        for (int i = 0; i < n; i++)
            if (dfn[i] == -1)
                dfs(i);

        scc.resize(cnt);
        for (int i = 0; i < n; i++)
            scc[iscc[i]].push_back(i);
        sort(scc.begin(), scc.end());
    }
};

signed main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    SCC scc(n);
    while (m--)
    {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        scc.add(a, b);
    }
    scc.build();
    cout << scc.cnt << endl;
    for (auto i : scc.scc)
    {
        for (auto j : i)
            cout << j + 1 << " ";
        cout << -1 << endl;
    }
    return oOvOo;
}
