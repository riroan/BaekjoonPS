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
    vector<vector<int>> arr(n, vector<int>(n, 10000000));
    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        arr[--a][--b] = 1;
        arr[b][a] = 1;
    }
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);
    int mm = numeric_limits<int>::max();
    int a, b;
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            ll tmp = 0;
            for (int k = 0; k < n; k++)
            {
                if (i == k || j == k)
                    continue;
                tmp += min(arr[i][k] * 2, arr[j][k] * 2);
            }
            if (mm > tmp)
            {
                mm = tmp;
                a = i + 1;
                b = j + 1;
            }
        }
    }
    cout << a << " " << b << " " << mm << endl;
    return oOvOo;
}