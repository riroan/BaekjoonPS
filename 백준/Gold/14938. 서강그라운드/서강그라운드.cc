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
    int n, m, r;
    cin >> n >> m >> r;
    vector<vector<int>> arr(n, vector<int>(n, numeric_limits<int>::max() / 10));
    vector<int> brr(n);
    for (auto &i : brr)
        cin >> i;
    for (int i = 0; i < r; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        arr[--a][--b] = c;
        arr[b][a] = c;
    }
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (i == j || j == k || k == i)
                    continue;
                else
                    arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);

    int ans = 0;
    for (int i = 0; i < n; i++)
    {
        int tmp = brr[i];
        for (int j = 0; j < n; j++)
            if (arr[i][j] <= m)
                tmp += brr[j];
        ans = max(ans, tmp);
    }
    cout << ans << endl;
    return oOvOo;
}