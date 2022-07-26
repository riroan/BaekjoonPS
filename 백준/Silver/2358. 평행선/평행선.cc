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
    map<int, int> x, y;
    while(n--){
        int a, b;
        cin >> a >> b;
        x[a]++;
        y[b]++;
    }
    ll ans = 0;
    for(auto [u,v]:x)
        if(v>=2)
            ans++;
    for(auto[u,v]:y)
        if(v>=2)
            ans++;
    cout << ans << endl;
    return oOvOo;
}