/**
 *    author:  riroan
 *    created:  2023.10.28 19:20:38
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
    vector<int> arr(n);
    auto go = [&](auto self, const vector<int> &brr) -> vector<int>
    {
        if (brr.size() == 1)
            return vector<int>({1});
        else if (brr.size() == 2)
            return vector<int>({1, 2});
        else if (brr.size() == 3)
            return vector<int>({1, 3, 2});
        int sz = brr.size();
        vector<int> a(sz / 2 + (sz % 2)), b(sz / 2);
        iota(a.begin(), a.end(), 1);
        iota(b.begin(), b.end(), 1);
        a = self(self, a);
        b = self(self, b);
        for (auto &i : a)
            i = i * 2 - 1;
        for (auto &i : b)
            i = i * 2;
        vector<int> res;
        for (auto i : a)
            res.push_back(i);
        for (auto i : b)
            res.push_back(i);
        return res;
    };
    iota(arr.begin(), arr.end(), 1);
    arr = go(go, arr);
    for (auto i : arr)
        cout << i << " ";
    cout << endl;
    return oOvOo;
}
