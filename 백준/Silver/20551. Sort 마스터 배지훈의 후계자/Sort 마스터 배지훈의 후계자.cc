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
    int n, m;
    cin >> n >> m;
    vector<int> arr(n);
    for(auto& i : arr)
        cin >> i;
    arr.push_back(numeric_limits<int>::max());
    sort(arr.begin(), arr.end());
    while(m--){
        int x;
        cin >> x;
        int ix = lower_bound(arr.begin(), arr.end(), x) - arr.begin();
        if(arr[ix]!= x)
            cout << -1 << endl;
        else
            cout << ix << endl;
    }
    return oOvOo;
}