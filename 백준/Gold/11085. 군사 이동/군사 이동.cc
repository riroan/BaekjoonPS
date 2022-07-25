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
    DisjointSet ds(n);
    int s, e;
    cin >> s >> e;
    vector<vector<int>> g(m);
    for (int i = 0; i < m; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        g[i] = vector<int>({-c, a, b});
    }
    sort(g.begin(), g.end());
    int ans = 0;
    for (int i = 0; i < m; i++)
    {
        int c, a, b;
        c = g[i][0];
        a = g[i][1];
        b = g[i][2];
        ds.unite(a, b);
        if(ds.get(s) == ds.get(e)){
            ans = -c;
            break;
        }
    }
    cout << ans << endl;

    return oOvOo;
}