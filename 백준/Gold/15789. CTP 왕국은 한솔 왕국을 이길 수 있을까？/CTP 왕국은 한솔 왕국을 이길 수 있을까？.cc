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
    int n, m;
    cin >> n >> m;
    DisjointSet ds(n);
    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        ds.unite(a, b);
    }
    int c, h, k;
    cin >> c >> h >> k;
    c--;
    h--;
    int cc = ds.get(c), hh = ds.get(h);
    int ans = 0;
    for (int i = 0; i < n;i++)
        if(cc == ds.get(i))
            ans++;
    vector<int> v;
    map<int, int> mp;
    for (int i = 0; i < n; i++)
        mp[ds.get(i)]++;
    for (auto [x,y]:mp)
        if(x != cc && x!= hh)
            v.push_back(y);
    sort(v.begin(), v.end());
    reverse(v.begin(), v.end());
    for (int i = 0; i < min(k, int(v.size()));i++)
        ans += v[i];
    cout << ans << endl;
    return oOvOo;
}
