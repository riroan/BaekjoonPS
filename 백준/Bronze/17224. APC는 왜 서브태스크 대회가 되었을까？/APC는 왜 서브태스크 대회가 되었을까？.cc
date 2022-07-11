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
    int n, l, k;
    cin >> n >> l >> k;
    vector<pair<int, int>> arr(n);
    for(auto& i : arr)
        cin >> i.second >> i.first;
    sort(arr.begin(), arr.end());
    int ans = 0;
    for(auto i : arr){
        if(k == 0)
            break;
        if (l >= i.first)
        {
            ans += 140;
            k--;
        }
        else if (l >= i.second)
        {
            ans += 100;
            k--;
        }
    }
    cout << ans << endl;
    return oOvOo;
}