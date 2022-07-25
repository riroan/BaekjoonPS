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
    vector<vector<char>> arr(n, vector<char>(m));
    for (auto &i : arr)
        for (auto &j : i)
            cin >> j;
    DisjointSet ds(n * m);
    auto f = [&](int x, int y)
    {
        return x * m + y;
    };
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            char ch = arr[i][j];
            int x = i, y = j;
            if (ch == 'L')
                y--;
            else if (ch == 'R')
                y++;
            else if (ch == 'U')
                x--;
            else
                x++;
            ds.unite(f(x, y), f(i, j));
        }
    }
    set<int> s;
    for (auto i = 0; i < n;i++)
        for (auto j = 0; j < m;j++)
            s.insert(ds.get(f(i, j)));
    cout << s.size() << endl;
    return oOvOo;
}