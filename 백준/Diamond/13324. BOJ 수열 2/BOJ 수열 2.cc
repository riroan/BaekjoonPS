#include <cstdio>
#include <queue>
using namespace std;

typedef long long ll;

int main() {
    ll n;
    scanf("%lld",&n);
    ll * arr = new ll[n];
    ll s = 0;
    for(int i=0;i<n;i++){
        scanf("%lld",&arr[i]);
        arr[i]-=i;
    }
    ll * brr = new ll[n];
    priority_queue<ll> pq;
    for(int i=0;i<n;i++){
        pq.push(arr[i]);
        pq.push(arr[i]);
        pq.pop();
        brr[i] = pq.top();
    }
    for (int i=n-2;i>=0;i--)
        if (brr[i] > brr[i+1])
            brr[i] = brr[i+1];
            
    for(int i=0;i<n;i++)
        printf("%lld\n",brr[i]+i);
}