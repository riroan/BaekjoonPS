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
    vector<vector<int>> arr(n, vector<int>(n));
    while(m--){
        int a, b, c;
        cin >> a >> b >> c;
        arr[--a][--b] = c;
    }
    int r;
    cin >> r;
    vector<int> brr(r);
    for(auto& i : brr){
        cin >> i;
        i--;
    }
    for (auto &i : arr)
        for(auto& j : i){
            if(j==0)
                j = 10000;
        }
    for (int k = 0; k < n;k++)
        for (int i = 0; i < n;i++)
            for (int j = 0; j < n;j++)
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);

    for (int i = 0; i < n; i++)
        arr[i][i] = 0;
    m = numeric_limits<int>::max() / 3;
    for (int i = 0; i < n;i++){
        int tmp = 0;
        for (auto j : brr){
            tmp = max(tmp, arr[i][j] + arr[j][i]);
        }
        m = min(m, tmp);
    }
    vector<int> ans;
    for (int i = 0; i < n; i++)
    {
        int tmp = 0;
        for (auto j : brr)
            tmp = max(tmp, arr[i][j] + arr[j][i]);
        if(tmp == m)
            ans.push_back(i + 1);
    }
    for (auto i = 0; i < ans.size(); i++)
        cout << ans[i] << " \n"[ans.size() - 1 == i];

    return oOvOo;
}