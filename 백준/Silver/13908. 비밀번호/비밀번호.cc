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
    vector<int> arr(m);
    for (auto &i : arr)
        cin >> i;
    int ans = 0;
    int uu = pow(10, n - 1);
    int tt = pow(10, n);
    for (int i = 0; i < tt; i++)
    {
        int u = i;
        int cnt[11] = {0};
        if (i < uu)
            cnt[0]++;
        while (u)
        {
            cnt[u % 10]++;
            u /= 10;
        }

        int ok = 1;
        for(auto i : arr){
            if(cnt[i] == 0)
                ok = 0;
        }
        ans += ok;
    }
    cout << ans << endl;
    return oOvOo;
}