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
    int n;
    cin >> n;
    map<string, int> mp;
    for (int i = 0; i < 2 * n - 1;i++){
        string s;
        cin >> s;
        mp[s]++;
    }
    for(auto [x, y] : mp){
        if(y%2)
            cout << x << endl;
    }
    return oOvOo;
}