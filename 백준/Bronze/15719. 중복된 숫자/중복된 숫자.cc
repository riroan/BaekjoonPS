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
    vector<int> arr(n);
    for(auto& i : arr)
        cin>>i;
    vector<bool> mp(10000001);
    for (auto i : arr)
        if(mp[i]){
            cout << i << endl;
            break;
        }else
            mp[i] = true;
    return oOvOo;
}