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
    int n, s;
    cin >> n >> s;
    vector<int> arr(n);
    for (auto &i : arr)
        cin >> i;
    sort(arr.begin(), arr.end());
    int ans = 0;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n;j++){
            if(arr[i]+ arr[j] <= s)
                ans++;
            else
                break;
        }
    cout << ans << endl;
    return oOvOo;
}