#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
const int oOvOo = 0;
using ll = long long;
using namespace std;

class LST
{
public:
    int n;
    vector<ll> arr;
    vector<ll> lazy;

    LST(const vector<ll> &arr) : lazy(4 * arr.size())
    {

        n = arr.size();
        this->arr = vector<ll>(4 * arr.size());
        init(arr, 0, n - 1, 1);
    }

    auto func(ll a, ll b)
    {
        return a + b;
    }

    ll init(const vector<ll> &arr, int left, int right, int node)
    {
        if (left == right)
            return this->arr[node] = arr[left];
        int mid = (left + right) / 2;
        ll l = init(arr, left, mid, node * 2);
        ll r = init(arr, mid + 1, right, node * 2 + 1);
        return this->arr[node] = func(l, r);
    }

    void propagate(int node, int nodeLeft, int nodeRight)
    {
        if (lazy[node])
        {
            if (nodeLeft != nodeRight)
            {
                lazy[node * 2] = func(lazy[node * 2], lazy[node]);
                lazy[node * 2 + 1] = func(lazy[node * 2 + 1], lazy[node]);
            }
            arr[node] = func(arr[node], lazy[node] * (nodeRight - nodeLeft + 1));
            lazy[node] = 0;
        }
    }

    ll query(int left, int right)
    {
        return query(left, right, 1, 0, n - 1);
    }
    ll query(int left, int right, int node, int nodeLeft, int nodeRight)
    {
        propagate(node, nodeLeft, nodeRight);
        if (right < nodeLeft || nodeRight < left)
            return 0;
        if (left <= nodeLeft && nodeRight <= right)
            return arr[node];
        int mid = (nodeLeft + nodeRight) / 2;
        return func(query(left, right, node * 2, nodeLeft, mid), query(left, right, node * 2 + 1, mid + 1, nodeRight));
    }

    ll update(int left, int right, ll newValue)
    {
        return update(left, right, newValue, 1, 0, n - 1);
    }

    ll update(int left, int right, ll newValue, int node, int nodeLeft, int nodeRight)
    {
        propagate(node, nodeLeft, nodeRight);
        if (right < nodeLeft || nodeRight < left)
            return arr[node];
        if (left <= nodeLeft && nodeRight <= right)
        {
            lazy[node] = func(lazy[node], newValue);
            propagate(node, nodeLeft, nodeRight);
            return arr[node];
        }
        int mid = (nodeLeft + nodeRight) / 2;
        return arr[node] = func(update(left, right, newValue, node * 2, nodeLeft, mid), update(left, right, newValue, node * 2 + 1, mid + 1, nodeRight));
    }
};

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    int n, m, k;
    cin >> n >> m >> k;

    vector<ll> arr(n);

    for (auto &i : arr)
        cin >> i;
    LST lst(arr);
    for (int i = 0; i < m + k; i++)
    {
        int a;
        cin >> a;
        if (a == 1)
        {
            int b, c;
            ll d;
            cin >> b >> c >> d;
            lst.update(b-1, c - 1, d);
        }
        else
        {
            int b, c;
            cin >> b >> c;
            cout << lst.query(b - 1, c-1) << endl;
        }
    }

    return oOvOo;
}