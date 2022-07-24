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
    int test;
    cin >> test;
    for (int tc = 1; tc <= test;++tc){
        int n;
        cin >> n;
        vector<tuple<int, int, int>> arr(n);
        for(auto& i : arr){
            int a, b, c;
            cin >> a >> b >> c;
            i = make_tuple(a, b, c);
        }
        DisjointSet ds(n);
        for (int i = 0; i < n;i++){
            for (int j = i+1; j < n;j++){
                auto [x1, y1, r1] = arr[i];
                auto [x2, y2, r2] = arr[j];
                if ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) <= (r1 + r2) * (r1 + r2))
                    ds.unite(i, j);
            }
        }
        set<int> s;
        for (int i = 0; i < n;i++)
            s.insert(ds.get(i));
        cout << s.size() << endl;
    }
    return oOvOo;
}