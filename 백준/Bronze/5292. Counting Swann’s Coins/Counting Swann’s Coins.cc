/**
 *    author:  riroan
 *    created:  2023.12.07 21:54:35
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
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		if(i%3 == 0)
			cout << "Dead";
		if(i%5==0)
			cout << "Man";
		if (i%3==0 || i%5==0)
			cout << "\n";
		else
			cout << i<<" ";
	}
	return oOvOo;
}
