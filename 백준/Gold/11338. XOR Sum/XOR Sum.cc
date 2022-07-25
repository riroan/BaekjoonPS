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
    int test;
    cin >> test;
    for (int tc = 1; tc <= test;++tc){
        int q, k;
        priority_queue<int, vector<int>, greater<int>> pq;
        int ans = 0;
        cin >> q >> k;
        while(q--){
            string op;
            cin >> op;
            if(op == "insert"){
                int x;
                cin >> x;
                if(pq.size()>=k){
                    if(pq.top()<x){
                        ans ^= pq.top();
                        ans ^= x;
                        pq.pop();
                        pq.push(x);
                    }
                }else{
                    ans ^= x;
                    pq.push(x);
                }
            }
            else
                cout << ans << endl;
        }
    }
    return oOvOo;
}