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
    vector<ll> arr(n);
    for(auto& i : arr)
        cin >> i;
    auto lis = [&]()
    {
        vector<ll> brr(1, numeric_limits<ll>::min());
        for (int i = 0; i < n;i++)
        {
            if(arr[i]>brr[brr.size()-1])
            {
                brr.push_back(arr[i]);
                continue;
            }
            auto t = lower_bound(brr.begin(), brr.end(), arr[i]) - brr.begin();
            brr[t] = arr[i];
        }
        return brr;
    };
    auto brr = lis();
    cout << brr.size()-1;
    return oOvOo;
}