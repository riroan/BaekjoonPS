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
        int n;
        cin >> n;
        vector<tuple<int, int>> arr(n);
        for (int i = 0; i < n;i++){
            int a, b;
            cin >> a >> b;
            arr[i] = {a, b};
        }
        sort(arr.begin(), arr.end());
        priority_queue<int> pq;
        int ans = 0;
        for (auto [x, y] : arr)
        {
            if (!pq.empty())
                if (-pq.top() < y)
                    ans++;
            pq.push(-y);
        }
        cout << n-ans << endl;
    }
    return oOvOo;
}