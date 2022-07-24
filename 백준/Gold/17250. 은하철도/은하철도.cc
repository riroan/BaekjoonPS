#include<bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
const int oOvOo=0;
using ll = long long;
using namespace std;
class DisjointSet{
public:
    vector<int> p;
    int n;
    DisjointSet(int _n) : n(_n){
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
int main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<ll> arr(n);
    for(auto &i : arr)
        cin >> i;
    DisjointSet ds(n);
    map<ll, ll> mp;
    for (auto i = 0; i < n;i++){
        mp[ds.get(i)] = arr[i];
    }
    while (m--)
    {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        bool ok = true;
        if(ds.get(a) == ds.get(b))
            ok = false;
        ll aa = mp[ds.get(a)];
        ll bb = mp[ds.get(b)];
        if(ok)
            cout << aa+bb << endl;
        else
            cout << aa << endl;
        if (ok){
            mp[ds.get(a)] += bb;
            mp[ds.get(b)] += aa;
            ds.unite(a, b);
        }
    }
    return oOvOo;
}
