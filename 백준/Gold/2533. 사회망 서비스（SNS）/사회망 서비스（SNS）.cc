#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
const int oOvOo = 0;
using ll = long long;
using namespace std;

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n;
    cin >> n;
    vector<vector<int>> g(n);
    for (auto i = 0; i < n - 1; i++)
    {
        int a, b;
        cin >> a >> b;
        g[--a].push_back(--b);
        g[b].push_back(a);
    }
    vector<int> dp(n);
    int root = 0;
    for (int i = 0; i < n; i++)
        if (g[i].size() >= 2)
        {
            root = i;
            break;
        }
    int answer = 0;
    function<int(int, int)> dfs = [&](int x, int p)
    {
        if (g[x].size() == 1)
            return 1;
        int u = 0;
        for (auto i : g[x])
        {
            if (i == p)
                continue;
            u |= dfs(i, x);
        }
        if (u)
            answer++;
        return 1 - u;
    };
    if (n == 2)
        cout << 1 << endl;
    else
    {
        dfs(root, -1);
        cout << answer << endl;
    }

    return oOvOo;
}