/**
 *    author:  riroan
 *    created:  2023.12.23 11:57:21
**/
#include<bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
#define int long long
const int oOvOo=0;
using ll = long long;
using namespace std;

signed main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int q;
    cin >> q;
    priority_queue<int> pq;
    while(q--){
        int a;
        cin >> a;
        if (a == 0){
            if(pq.empty()){
                cout << -1 << endl;
            }else{
                cout << pq.top() << endl;
                pq.pop();
            }
        }else{
            while(a--){
                int x;
                cin >> x;
                pq.push(x);
            }
        }
    }
    return oOvOo;
}
