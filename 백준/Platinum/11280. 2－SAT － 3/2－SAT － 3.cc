/**
 *    author:  riroan
 *    created:  2023.12.03 15:50:48
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
    vector<vector<int>> g;
    vector<int> stk;
    vector<int> dfn, low, iscc;
    vector<vector<int>> scc;
    vector<pair<int, int>> edges;
    vector<vector<int>> arr; // SCC graph
    int cur, cnt;

    SCC() {}
    SCC(int n)
    {
        init(n);
    }

    void init(int n)
    {
        this->n = n;
        g.assign(n, {});
        dfn.assign(n, -1);
        low.resize(n);
        iscc.assign(n, -1);
        stk.clear();
        cur = cnt = 0;
    }

    void add(int u, int v)
    {
        edges.push_back({u, v});
        g[u].push_back(v);
    }

    int dfs(int x)
    {
        dfn[x] = low[x] = cur++;
        stk.push_back(x);

        for (auto y : g[x])
            if (dfn[y] == -1)
                low[x] = min(low[x], dfs(y));
            else if (iscc[y] == -1)
                low[x] = min(low[x], dfn[y]);

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
        return low[x];
    }

    void build()
    {
        for (int i = 0; i < n * 2; i++)
            if (dfn[i] == -1)
                dfs(i);

        scc.resize(cnt);
        for (int i = 0; i < n; i++)
            scc[iscc[i]].push_back(i);
        sort(scc.begin(), scc.end());
        arr.resize(cnt);

        for (auto [x, y] : edges)
            if (iscc[x] != iscc[y])
                arr[iscc[x]].push_back(iscc[y]);
    }
};

struct SAT : public SCC
{
    SAT(int n)
    {
        n++;
        init(n);
    }
    void init(int n)
    {
        this->n = n;
        g.assign(n * 2, {});
        dfn.assign(n * 2, -1);
        low.resize(n * 2);
        iscc.assign(n * 2, -1);
        stk.clear();
        cur = cnt = 0;
    }

    int apply_not(int a)
    {
        return a % 2 ? a - 1 : a + 1;
    }

    void add(int u, int v)
    {
        u = (u < 0 ? -(u + 1) * 2 : u * 2 - 1);
        v = (v < 0 ? -(v + 1) * 2 : v * 2 - 1);
        g[apply_not(u)].push_back(v);
        g[apply_not(v)].push_back(u);
    }

    auto check()
    {
        for (int i = 0; i < n; i++)
            if (iscc[i * 2] == iscc[i * 2 + 1])
                return 0;
        return 1;
    }
};

signed main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    SAT sat(n + 1);
    while (m--)
    {
        int a, b;
        cin >> a >> b;
        sat.add(a, b);
    }
    sat.build();
    cout << sat.check() << endl;
    return oOvOo;
}
