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
    vector<vector<int>> arr(n, vector<int>(n));
    for (int i = 0; i < m; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        a--;
        b--;
        arr[a][b] = c;
        arr[b][a] = c;
    }
    for (auto &i : arr)
        for (auto &j : i)
        {
            if (j == 0)
                j = 10000000;
        }
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);
    int ans = numeric_limits<int>::max();
    int ix = 0;
    for (int i = 0; i < n; i++)
    {
        int tmp = 0;
        for (int j = 0; j < n; j++)
            if (i != j)
                tmp += arr[i][j];
        if (tmp < ans)
        {
            ans = tmp;
            ix = i;
        }
    }
    cout << ix + 1;
    return oOvOo;
}