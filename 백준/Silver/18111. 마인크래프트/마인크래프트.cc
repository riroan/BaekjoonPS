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
    int n, m, b;
    cin >> n >> m >> b;
    vector<vector<int>> arr(n, vector<int>(m));
    for (int i = 0;i<n;i++){
        for (int j = 0; j < m;j++)
            cin >> arr[i][j];
    }
    int ans = 987654321;
    int aans = 0;
    int mm = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0;j<m;j++)
            mm = max(mm, arr[i][j]);
    for (int i = mm; i >= 0;i--){
        int cnt = 0;
        for (int j = 0; j < n;j++){
            for (int k = 0; k < m;k++)
                cnt += i - arr[j][k];
        }
        if(cnt>b)
            continue;
        int sec = 0;
        for (int j = 0; j < n;j++){
            for (int k = 0; k < m;k++){
                if(i>arr[j][k])
                    sec += i - arr[j][k];
                else
                sec+=2*(arr[j][k]-i);
            }
        }
        if(ans>sec){
            ans = sec;
            aans = i;
        }
    }
    cout << ans << " " << aans << endl;

    return oOvOo;
}