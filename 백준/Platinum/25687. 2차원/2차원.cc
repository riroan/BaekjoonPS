/**
 *    author:  riroan
 *    created:  2023.10.28 20:34:17
 **/
#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
#define int long long
const int oOvOo = 0;
using ll = long long;
using namespace std;

signed main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n;
    cin >> n;
    vector<vector<int>> arr(n, vector<int>(n));
    int ix = 1;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            arr[j][(i + j) % n] = ix++;
    for(auto i : arr){
        for(auto j : i)
            cout << j << " ";
        cout << endl;
    }
    return oOvOo;
}
