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
    vector<string> arr(n);
    for(auto& i : arr)
        cin >> i;
    int k;
    vector<deque<int>> q(n);
    for (int i = 0; i < n;i++)
        for(auto j : arr[i])
            q[i].push_back(j - '0');
    cin >> k;
    while(k--){
        int x, d;
        cin >> x >> d;
        x--;
        vector<int> can({x});
        for (int i = x + 1; i < n;i++){
            if (q[i][6] != q[i-1][2])
                can.push_back(i);
            else
                break;
        }
        for (int i = x - 1; i >= 0;i--){
            if(q[i][2] != q[i+1][6])
                can.push_back(i);
            else
                break;
        }
        sort(can.begin(), can.end());
        
        for (auto i : can)
        {
            if (i % 2 == x % 2 && d == 1 || i % 2 != x % 2 && d == -1)
            {
                q[i].push_front(q[i].back());
                q[i].pop_back();
            }
            else
            {
                q[i].push_back(q[i].front());
                q[i].pop_front();
            }
        }
    }
    int ans = 0;
    for (auto i : q)
        ans += i.front();
    cout << ans << endl;
    return oOvOo;
}