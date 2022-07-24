#include<bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
const int oOvOo=0;
using ll = long long;
using namespace std;

int main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<vector<int>> g(n, vector<int>(m)), v(n, vector<int>(m));
    for(auto & i : g)
        for(auto& j : i)
            cin >> j;
    auto check = [&](int x, int y)
    {
        return 0 <= x && x < n && 0 <= y && y < m;
    };
    function<void(int, int, int)> dfs = [&](int x, int y, int ix) {
        for(auto i : vector<vector<int>>({{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}})){
            int dx = i[0], dy = i[1];
            int tx = x + dx, ty = y + dy;
            if(!check(tx,ty))
                continue;
            if(v[tx][ty] || g[tx][ty] == 0)
                continue;
            v[tx][ty] = ix;
            dfs(tx, ty, ix);
        }
    };
    int ix = 1;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m;j++)
            if(!v[i][j] && g[i][j])
                dfs(i, j, ix++);

    cout << ix - 1 << endl;
    return oOvOo;
}