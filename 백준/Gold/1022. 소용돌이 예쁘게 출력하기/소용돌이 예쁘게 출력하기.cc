#include<bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
const int oOvOo=0;
using ll = long long;
using namespace std;

int main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int a, b, c, e;
    cin >> a >> b >> c >> e;
    vector<vector<int>> ans(c-a+1, vector<int>(e-b+1));
    short x = 5000, y = 5000;
    vector<vector<char>> d({{0, 1}, {-1, 0}, {0, -1}, {1, 0}});
    int t = 0;
    int ix = 1;
    int number = 0;
    int tmp = 0;
    int tt = 0;
    int u;
    while (x < 10001 && y < 10001)
    {
        int dx = d[t][0], dy = d[t][1];
        x += dx, y += dy;
        ix++;
        if (a + 5000 <= x && x <= c + 5000 && b + 5000 <= y && y <= e + 5000)
            ans[x-5000-a][y-5000-b] = ix;
        if(tmp != number)
            tmp++;
        else{
            if (tt){
                number++;
                tt = 0;
            }
            else
                tt = 1;
            t = (t + 1) % 4;
            tmp = 0;
        }
    }
    int mm = 0;
    for(auto i : ans)
        for(auto j : i)
            mm = max(mm, j);
    auto f = [](int x)
    {
        int r = 0;
        while(x)
        {
            x /= 10;
            r++;
        }
        return r;
    };

    int len = f(mm);
    for (auto i : ans)
    {
        for (auto j : i){
            for (int k = 0; k < len - f(max(j, 1));k++)
                cout << " ";
            cout << (j == 0 ? 1 : j) << " ";
        }
        cout << endl;
    }
}