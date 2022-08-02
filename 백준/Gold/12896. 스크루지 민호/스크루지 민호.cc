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
    int n;
    cin >> n;
    vector<vector<int>> g(n);
    for (int i = 0; i < n-1;i++){
        int a, b;
        cin >> a >> b;
        g[--a].push_back(--b);
        g[b].push_back(a);
    }
    int m = 0, ix;
    vector<int> path;
    function<void(int, int, int)> dfs = [&](int x, int p, int d)
    {
        if (m < d){
            m = d;
            ix = x;
        }
        for(auto i :g[x]){
            if(i==p)
                continue;
            dfs(i, x, d+1);
        }
    };
    dfs(0, -1, 0);
    m = 0;
    dfs(ix, -1, 0);
    cout << (m + 1) / 2 << endl;
    // function<void(int, int, int)> dfs1 = [&](int x, int p, int d)
    // {
    //     ret = max(ret, d);
    //     for(auto i : g[x]){
    //         if(i==p)
    //             continue;
    //         dfs1(i, x, d + 1);
    //     }
    // };
    // dfs1(ix, -1, 0);
    // cout << ret << endl;
    return oOvOo;
}