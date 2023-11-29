/**
 *    author:  riroan
 *    created:  2023.11.29 21:55:37
 **/
#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
#define int long long
const int oOvOo = 0;
using ll = long long;
using namespace std;

int ipow(int x, int r, int mod)
{
    if (r == 1)
        return x;
    int t = ipow(x, r / 2, mod);
    if (r % 2)
        return (((t * t) % mod) * x) % mod;
    return (t * t) % mod;
}

struct Z
{
    int mod;
    int x;
    Z() : Z(0, 0)
    {
    }
    Z(int a, int mod)
    {
        x = a;
        this->mod = mod;
    }
    Z operator+(int r)
    {
        return *this + Z(r, mod);
    }
    Z operator+(Z r)
    {
        return Z((x + r.x) % mod, mod);
    }
    Z operator-(int r)
    {
        return *this - Z(r, mod);
    }
    Z operator-(Z r)
    {
        int v = x - r.x;
        if (v < 0)
            v += mod;
        return Z(v, mod);
    }
    Z operator*(int r)
    {
        return *this * Z(r, mod);
    }
    Z operator*(Z r)
    {
        int v = (x * r.x) % mod;
        return Z(v, mod);
    }
    Z inv()
    {
        return Z(ipow(x, mod - 2, mod), mod);
    }
    Z operator/(Z r)
    {
        return *this * r.inv();
    }
    Z operator-()
    {
        return Z(-x, mod);
    }
    void operator=(Z r)
    {
        x = r.x;
    }
    bool operator!=(Z r)
    {
        return x != r.x;
    }
    void operator+=(Z r)
    {
        x = (x + r.x) % mod;
    }
    void operator*=(Z r)
    {
        x = (x * r.x) % mod;
    }
};

signed main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    Z s(b, a), x(c, a), y(d, a);
    Z cc = ((x * x - y * s) / (x - s));
    cout << ((y - cc) / x).x << " " << cc.x;
    return oOvOo;
}
