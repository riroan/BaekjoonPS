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
    vector<vector<int>> v(m);
    for (int i = 0; i < m;i++){
        int a, b, c;
        cin >> a >> b >> c;
        v[i] = vector<int>({--a, --b, c});
    }
    sort(v.begin(), v.end(), [](const vector<int >& a, const vector<int>& b) {
        if(b[2] == a[2]){
            if(a[1] == b[1])
                return a[0] > b[0];
            return a[1] > b[1];
        }
        else
        {
            return a[2] > b[2];
        }
    });
    int ans = 0;
    int start, end;
    cin >> start >> end;
    start--;
    end--;
    for (auto i : v)
    {
        int x = i[0], y = i[1], z = i[2];
        ds.unite(x, y);
        if(ds.get(start) == ds.get(end)){
            ans = z;
            break;
        }
    }
    cout << ans << endl;
    return oOvOo;
}