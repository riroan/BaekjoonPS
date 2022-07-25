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
    vector<pair<int, int>> p(n);
    for (auto &i : p)
        cin >> i.first >> i.second;
    vector<vector<int>> arr(n, vector<int>(n));
    for (auto &i : arr)
        for (auto &j : i)
        {
            if (j == 0)
                j = 100000000;
        }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == j)
                continue;
            int x1 = p[i].first, y1 = p[i].second, x2 = p[j].first, y2 = p[j].second;
            if (min(y1, y2) >= max(x1, x2))
            {
                arr[i][j] = 1;
                arr[j][i] = 1;
            }
        }
    }
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);
    int q;
    cin >> q;
    while (q--)
    {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        int ans = arr[a][b];
        if(ans == 100000000)
            ans = -1;
        cout << ans << endl;
    }
    return oOvOo;
}