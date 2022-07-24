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
    int n;
    cin >> n;
    DisjointSet ds(1000010);
    map<ll, ll> mp;
    for (int i = 0; i < 1000010; i++)
        mp[i] = 1;
    while (n--)
    {
        char ch;
        cin >> ch;
        if(ch == 'I'){
            int a, b;
            cin >> a >> b;
            a--;
            b--;
            if(ds.get(a) != ds.get(b)){
                int aa = mp[ds.get(a)];
                int bb = mp[ds.get(b)];
                mp[ds.get(a)] += bb;
                mp[ds.get(b)] += aa;
                ds.unite(a, b);
            }
        }
        else
        {
            int x;
            cin >> x;
            cout << mp[ds.get(--x)] << endl;
        }
    }
    return oOvOo;
}