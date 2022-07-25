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
    vector<int> arr(n);
    DisjointSet ds(n);
    map<int, int> mp;
    for (int i = 0; i < n;i++){
        int x;
        cin >> x;
        arr[i] = x;
        mp[i] = x;
    }
    for (int i = 0; i < m; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        b--;
        c--;
        if (a == 1)
        {
            int bb = mp[ds.get(b)], cc = mp[ds.get(c)];
            mp[ds.get(b)] += cc;
            mp[ds.get(c)] += bb;
            ds.unite(b, c);
        }
        else
        {
            int bb = mp[ds.get(b)], cc = mp[ds.get(c)];
            int tmp = 0;
            if (bb > cc)
                tmp = bb - cc;
            else if (bb < cc)
                tmp = cc - bb;
            else
                tmp = 0;
            mp[ds.get(b)] = tmp;
            mp[ds.get(c)] = tmp;
            ds.unite(b, c);
        }
    }
    map<int, int> ans;
    for (int i = 0; i < n;i++){
        ans[ds.get(i)] = mp[ds.get(i)];
    }
    int cnt = 0;
    vector<int> tmp;
    for(auto [x,y] : ans){
        if (y){
            cnt++;
            tmp.push_back(y);
        }
    }
    cout << cnt << endl;
    sort(tmp.begin(), tmp.end());
    for(auto i : tmp)
        cout << i << " ";
    cout << endl;
    return oOvOo;
}