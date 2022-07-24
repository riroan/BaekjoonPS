#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
const int oOvOo = 0;
using ll = long long;
using namespace std;
#define int long long
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
int32_t main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n, m, k;
    cin >> n >> m >> k;
    vector<int> arr(n);
    for (auto &i : arr)
        cin >> i;
    set<pair<int, int>> s;
    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        if (a > b)
            swap(a, b);
        s.insert(make_pair(a-1, b-1));
    }
    DisjointSet ds(n);
    for (int i = 0; i < n; i++)
    {
        int a = i, b = (i + 1) % n;
        if (a > b)
            swap(a, b);
        if (s.find(make_pair(a, b)) == s.end())
            ds.unite(a, b);
    }
    if(m<=1)
    {
        cout << "YES" << endl;
        return 0;
    }
    map<int, vector<int>> v;
    for (int i = 0; i < n;i++)
        v[ds.get(i)].push_back(arr[i]);
    int cnt = 0;
    for (auto [x, y] : v)
    {
        if(y.size() == 0)
            continue;
        int mm = numeric_limits<int>::max();
        for (auto i : y)
            mm = min(mm, i);
        cnt += mm;
        if(cnt > k)
            break;
    }
    if(cnt <= k)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return oOvOo;
}