#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
using ll = long long;
using namespace std;

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    string s;
    map<string, int> m;
    set<string> ss;
    int cnt = 0;
    while (getline(cin, s))
    {
        m[s]++;
        ss.insert(s);
        cnt++;
    }
    vector<string> v;
    
    for(auto i : ss)
        v.push_back(i);
    sort(v.begin(), v.end());

    for (auto i : v)
    {
        cout.precision(4);
        printf("%s %.4lf\n",i.c_str(),  round((m[i] / (double)cnt) * 100 * 10000) / 10000);
    }
}