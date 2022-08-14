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
    cout << "? 1" << endl;
    cout.flush();
    int x, y;
    cin >> x;
    cout << "? " << n << endl;
    cout.flush();
    cin >> y;
    if (x == 1 && y == 0){
        cout << "! -1" << endl;
    }else if(x==y){
        cout << "! 0" << endl;
    }else{
        cout << "! 1" << endl;
    }
    cout.flush();
    return oOvOo;
}