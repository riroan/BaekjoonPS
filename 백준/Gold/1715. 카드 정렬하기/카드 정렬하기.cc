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
    priority_queue<int> pq;
    while(n--){
        int x;
        cin >> x;
        pq.push(-x);
    }
    ll ans = 0;
    while (pq.size() > 1)
    {
        int a = -pq.top();
        pq.pop();
        int b = -pq.top();
        pq.pop();
        pq.push(-(a + b));
        ans += a + b;
    }
    cout << ans << endl;

    return oOvOo;
}