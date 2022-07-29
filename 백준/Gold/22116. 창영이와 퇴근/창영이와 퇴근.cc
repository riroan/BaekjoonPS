#include<iostream>
#include<algorithm>
#include<vector>
#include<utility>
#include<numeric>
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
    int n;
    cin>>n;
    vector<vector<int>> arr(n, vector<int>(n));
    for(auto& i : arr)
        for(auto& j : i)
            cin >> j;
    auto get = [&](int x, int y)
    {
        return x * n + y;
    };
    auto check = [&](int x, int y)
    {
        return 0 <= x && x < n && 0 <= y && y < n;
    };
    vector<vector<int>>
        edges;
    for (int x = 0; x < n;x++){
        for (int y = 0; y < n;y++){
            for(auto [dx,dy] : vector<tuple<int, int>>({{1,0},{0,1}})){
                int tx = x + dx, ty = y + dy;
                if(!check(tx,ty))
                    continue;
                edges.push_back(vector<int>({abs(arr[x][y] - arr[tx][ty]) ,get(x, y), get(tx, ty)}));
            }
        }
    }
    sort(edges.begin(), edges.end());
    DisjointSet ds(n * n);
    int ans = 0;
    for(auto edge : edges){
        int x = edge[1], y = edge[2], d = edge[0];
        if(ds.get(x) != ds.get(y)){
            ds.unite(x, y);
            ans = max(ans, d);
        }
        if(ds.get(0) == ds.get(n*n-1))
            break;
    }
    cout << ans << endl;
    return oOvOo;
}