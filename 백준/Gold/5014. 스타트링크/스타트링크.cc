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
    int f, s, g, u, d;
    cin >> f >> s >> g >> u >> d;
    vector<int> dp(f + 1, numeric_limits<int>::max());
    function<void(int, int)> ff = [&](int x, int cnt)
    {
        if(x<1 || x> f)
            return;
        if (dp[x] <=cnt)
            return;
        dp[x] = min(dp[x], cnt);
        ff(x + u, cnt + 1);
        ff(x - d, cnt + 1);
    };
    ff(s, 0);
    if (dp[g] == numeric_limits<int>::max())
        cout << "use the stairs" << endl;
    else
        cout << dp[g] << endl;
    return oOvOo;
}