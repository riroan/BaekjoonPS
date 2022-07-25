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
    int n, m;
    cin >> n >> m;
    vector<int> arr(n);
    for(auto& i : arr)
        cin >> i;
    int q;
    cin >> q;
    vector<int> tmp(q);
    for(auto & i : tmp)
        cin >> i;
    vector<vector<int>> ans, g(n);
    for (int i = 0; i < n;i++){
        if (i != --arr[i])
            g[arr[i]].push_back(i);
    }
    cout << n << " " << m << endl;
    for (int i : tmp)
        cout << 2 << " " << i << endl;
    function<void(int)> dfs = [&](int x)
    {
        for(auto i : g[x]){
            ans.push_back({1, i + 1, x + 1});
            dfs(i);
        }
    };
    for (int i = 0; i < n;i++)
        if(arr[i] == i)
            dfs(i);
    for (int i = 0; i < m - ans.size() - tmp.size();i++)
        cout << "1 1 1" << endl;
    reverse(ans.begin(), ans.end());
    for (auto i : ans)
        for (int j = 0; j < i.size(); j++)
            cout << i[j] << " \n"[j == i.size() - 1];
    return oOvOo;
}