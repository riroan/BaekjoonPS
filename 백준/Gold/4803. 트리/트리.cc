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
    int test = 1;
    while (1){
        int n, m;
        cin >> n >> m;
        if(n+m==0)
            break;
        cout << "Case " << test++<<": ";
        DisjointSet ds(n);
        vector<vector<int>> g(n);
        for (int i = 0; i < m;i++){
            int a, b;
            cin >> a >> b;
            ds.unite(--a, --b);
            g[a].push_back(b);
            g[b].push_back(a);
        }
        int ans = 0;
        int mm = 0;
        set<int> s;
        for (int i = 0; i < n; i++)
        {
            int p = ds.get(i);
            mm = max(mm, p);
            s.insert(p);
        }
        for (auto i : s)
        {
            int cnt = 0;
            int tmp = 0;
            for (int j = 0; j < n; j++)
                if (ds.get(j) == i){
                    cnt += g[j].size();
                    tmp++;
                }
            if(cnt == 0)
                ans++;
            else if((tmp -1)*2 == cnt )
                ans++;
        }
        if(ans == 0)
            cout << "No trees." << endl;
        else if(ans == 1)
            cout << "There is one tree." << endl;
        else
            cout << "A forest of " << ans << " trees." << endl;
    }
    return oOvOo;
}