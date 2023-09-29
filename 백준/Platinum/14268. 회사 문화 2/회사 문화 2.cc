#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
#define int long long
const int oOvOo = 0;
using ll = long long;
using namespace std;

class Node
{
public:
    ll value = 0;
    ll lazy = 0;
};

class LST
{
public:
    int n;
    vector<Node> tree;

    LST(const vector<ll> &arr)
    {
        n = arr.size();
        tree = vector<Node>(4 * n);
        init(arr, 0, n - 1, 1);
    }

    auto func(ll a, ll b)
    {
        return a + b;
    }

    Node init(const vector<ll> &arr, int left, int right, int node)
    {
        if (left == right)
        {
            tree[node].value = arr[left];
            return tree[node];
        }
        int mid = (left + right) / 2;
        Node l = init(arr, left, mid, node * 2);
        Node r = init(arr, mid + 1, right, node * 2 + 1);
        tree[node].value = func(l.value, r.value);
        return tree[node];
    }

    void propagate(int node, int nodeLeft, int nodeRight)
    {
        if (tree[node].lazy)
        {
            if (nodeLeft != nodeRight)
            {
                tree[node * 2].lazy = func(tree[node * 2].lazy, tree[node].lazy);
                tree[node * 2 + 1].lazy = func(tree[node * 2 + 1].lazy, tree[node].lazy);
            }
            tree[node].value = func(tree[node].value, tree[node].lazy * (nodeRight - nodeLeft + 1));
            tree[node].lazy = 0;
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
            return tree[node].value;
        int mid = (nodeLeft + nodeRight) / 2;
        return func(query(left, right, node * 2, nodeLeft, mid), query(left, right, node * 2 + 1, mid + 1, nodeRight));
    }

    void update(int left, int right, ll newValue)
    {
        update(left, right, newValue, 1, 0, n - 1);
    }

    void update(int left, int right, ll newValue, int node, int nodeLeft, int nodeRight)
    {
        propagate(node, nodeLeft, nodeRight);
        if (right < nodeLeft || nodeRight < left)
            return;
        if (left <= nodeLeft && nodeRight <= right)
        {
            tree[node].lazy = func(tree[node].lazy, newValue);
            propagate(node, nodeLeft, nodeRight);
            return;
        }
        int mid = (nodeLeft + nodeRight) / 2;
        update(left, right, newValue, node * 2, nodeLeft, mid);
        update(left, right, newValue, node * 2 + 1, mid + 1, nodeRight);
        tree[node].value = func(tree[node * 2].value, tree[node * 2 + 1].value);
    }
};

signed main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<vector<int>> arr(n);
    int root = -1;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        if (x == -1)
        {
            root = i;
            continue;
        }
        x--;
        arr[x].push_back(i);
        arr[i].push_back(x);
    }
    vector<int> start(n), end(n);
    int cur = -1;
    auto dfs = [&](auto self, int x, int p) -> void
    {
        start[x] = ++cur;
        for (auto i : arr[x])
        {
            if (i == p)
                continue;
            self(self, i, x);
        }
        end[x] = cur;
    };
    dfs(dfs, root, root);
    vector<int> brr(n);
    LST lst(brr);
    while (q--)
    {
        int op;
        cin >> op;
        if (op == 1)
        {
            int a, b;
            cin >> a >> b;
            --a;
            lst.update(start[a], end[a], b);
        }
        else
        {
            int a;
            cin >> a;
            --a;
            cout << lst.query(start[a], start[a]) << endl;
        }
    }
    return oOvOo;
}
