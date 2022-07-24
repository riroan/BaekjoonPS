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
    vector<vector<int>> g(n);
    for (int i = 0; i < m;i++){
        int a, b;
        cin >> a >> b;
        g[--a].push_back(--b);
        g[b].push_back(a);
    }
    int q;
    cin >> q;
    while(q--){
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        g[a].push_back(b);
        g[b].push_back(a);
        vector<int> ans(n, -1);
        int start = 0;
        queue<tuple<int, int>> q;
        q.push(make_tuple(start, 0));
        vector<bool> v(n);
        v[start] = true;
        while (!q.empty())
        {
            auto [x, d] = q.front();
            ans[x] = d;
            q.pop();
            for(auto i : g[x]){
                if(v[i])
                    continue;
                v[i] = true;
                q.push(make_tuple(i, d + 1));
            }
        }
        for (int i = 0; i < n;i++)
            cout << ans[i] << " \n"[i == n - 1];
    }
    return oOvOo;
}