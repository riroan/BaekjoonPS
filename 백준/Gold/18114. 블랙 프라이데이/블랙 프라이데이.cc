#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
const int oOvOo = 0;
using ll = long long;
using namespace std;
int dd[100000001];
int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n, c;
    cin >> n >> c;
    vector<int> arr(n);
    for (auto &i : arr)
        cin >> i;
    for (auto i : arr) // O(n)
        dd[i]++;
    cout << [&]()
    {
        if (dd[c])
            return 1;
        for (int i = 0; i < n; i++) // O(n^2)
            for (int j = i + 1; j < n; j++)
            {
                dd[arr[i]]--;
                dd[arr[j]]--;
                if (arr[i] + arr[j] == c)
                    return 1;
                if ( c-arr[i]-arr[j]<0)
                    continue;
                if (dd[c - arr[i] - arr[j]])
                    return 1;
                dd[arr[i]]++;
                dd[arr[j]]++;
            }
        return 0;
    }() << endl;
    return oOvOo;
}