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
        cin >> i;
    vector<int> ps(1);
    for(auto i : arr)
        ps.push_back(ps[ps.size() - 1] + i);
    ll ans = 0;
    for (int i = n - 1; i > 0;i--){
        ans += arr[i] * ps[i];
    }
    cout << ans << endl;
    return oOvOo;
}