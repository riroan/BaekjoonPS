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
    while(test--){
        string s;
        cin >> s;
        list<char> l;
        auto iter = l.begin();
        int ix = 0;
        for (auto i : s)
        {
            if(i == '<'){
                if (ix>0){
                    iter--;
                    ix--;
                }
            }else if(i=='>'){
                if (ix < l.size()){
                    iter++;
                    ix++;
                }
            }else if(i == '-'){
                if(ix){
                    iter = l.erase(--iter);
                    ix--;
                }
            }else{
                l.insert(iter, i);
                ix++;
            }
        }
        for (auto i : l)
            cout << i;
        cout << endl;
    }
    return oOvOo;
}