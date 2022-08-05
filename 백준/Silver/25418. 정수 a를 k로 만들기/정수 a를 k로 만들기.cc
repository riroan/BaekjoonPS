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
    vector<int> dp(1000001, 1000000000);
    int a, k;
    cin >> a >> k;
    queue<tuple<int, int>> q;
    q.push({a, 0});
    while (!q.empty()){
        auto [x, y] = q.front();
        q.pop();
        if (dp[x] <= y)
            continue;
        dp[x] = y;
        if (x < 1000000)
            q.push({x + 1, y + 1});
        if(x <= 500000)
            q.push({2 * x, y + 1});
    }
    cout << dp[k] << endl;
    return oOvOo;
}