#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
const int oOvOo = 0;
using ll = long long;
using namespace std;
class DisjointSet
{
public:
    vector<int> p;
    int n;
    DisjointSet(int _n) : n(_n)
    {
        p.resize(n);
        iota(p.begin(), p.end(), 0);
    }

    inline int get(int x)
    {
        return (x == p[x] ? x : (p[x] = get(p[x])));
    }

    inline bool unite(int x, int y)
    {
        x = get(x);
        y = get(y);
        if (x != y)
        {
            p[x] = y;
            return true;
        }
        return false;
    }
};
int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n, m, k;
    cin >> n >> m >> k;
    vector<int> arr(n);
    for (auto &i : arr)
        cin >> i;
    DisjointSet ds(n);
    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        ds.unite(a, b);
    }
    map<int, vector<int>> mp;
    for (auto i = 0; i < n; i++)
        mp[ds.get(i)].push_back(arr[i]);
    int ans = 0;
    for (auto [x, y] : mp)
    {
        int mm = numeric_limits<int>::max();
        for (auto i : y)
            mm = min(mm, i);
        ans += mm;
    }
    if (ans <= k)
        cout << ans << endl;
    else
        cout << "Oh no" << endl;

    return oOvOo;
}