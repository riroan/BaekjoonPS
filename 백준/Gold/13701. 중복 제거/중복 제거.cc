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
    int arr[33554432/32] = {0};
    int a;
    do
    {
        scanf("%d", &a);
        if(arr[a/32] & (1<<(a%32)))
            continue;
        printf("%d ", a);
        arr[a / 32] |= 1 << a % 32;
    } while (getc(stdin) == ' ');
    return oOvOo;
}