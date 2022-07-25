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
        int a, b;
        cin >> a >> b;
        arr[--a][--b] = 1;
    }
    for (auto &i : arr)
        for (auto &j : i)
        {
            if (j == 0)
                j = numeric_limits<int>::max() / 3;
        }
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);
    int ans = 0;
    int mid = ceil(n / 2.0);
    for (int i = 0; i < n; i++)
    {
        int cnt1 = 0, cnt2 = 0;
        for (int j = 0; j < n; j++)
        {
            if(i==j)
                continue;
            if (arr[i][j] != numeric_limits<int>::max() / 3)
                cnt1++;
            if (arr[j][i] != numeric_limits<int>::max() / 3)
                cnt2++;
        }
        if(cnt1>=mid || cnt2>=mid)
            ans++;
    }
    cout << ans << endl;
    return oOvOo;
}