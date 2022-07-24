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
    string s;
    cin >> s;
    vector<int> arr;
    for (int i = 0; i < s.size();i++)
        arr.push_back(s[i] - '0');
    vector<int> ps(1);
    for(auto i :arr)
        ps.push_back(ps[ps.size() - 1] + i);
    int ans = 0;
    for (int i = 0; i <= s.size(); i += 2){
        // cout << i << endl;
        for (int j = 0; j + i <= s.size(); j++)
        {
            int a = ps[j + i / 2] - ps[j];
            int b = ps[j + i] - ps[j + i / 2];
            // cout << a << " " << b << endl;
            if (a == b)
                ans = i;
        }
    }
    cout << ans << endl;
    return oOvOo;
}