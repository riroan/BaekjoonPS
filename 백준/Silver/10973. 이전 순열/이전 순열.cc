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
    for(auto & i : arr)
        cin >> i;
    bool ok = true;
    for (int i = 0; i < n;i++)
        if (arr[i] != i+1)
            ok = false;
    if (ok){
        cout << -1 << endl;
        return 0;
    }
    prev_permutation(arr.begin(), arr.end());
    for(auto i : arr)
        cout << i << " ";
    cout << endl;
    return oOvOo;
}