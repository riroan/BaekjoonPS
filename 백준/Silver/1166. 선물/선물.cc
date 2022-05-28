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
    ll n, l, w, h;
    cin >> n >> l >> w >> h;
    long double left = 0, right = 1e9;
    while (left + 1e-10 < right){
        long double mid = (left + right) / 2;
        if(ll(l/mid)*ll(w/mid)*ll(h/mid)<n)
            right = mid;
        else
            left = mid;
    }
    cout.precision(12);
    cout << right << endl;
    return oOvOo;
}