#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
const int oOvOo = 0;
using ll = long long;
using namespace std;

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n;
    cin >> n;
    priority_queue<int> pq;
    while (n--)
    {
        int x;
        cin >> x;
        if (pq.size() < 4)
            pq.push(x);
        else
        {
            if (pq.top() > x)
            {
                pq.pop();
                pq.push(x);
            }
        }
    }
    vector<string> arr;
    while (!pq.empty())
    {
        arr.push_back(to_string(pq.top()));
        pq.pop();
    }
    vector<int> brr;
    for (int i = 0; i < arr.size(); i++)
    {
        for (int j = 0; j < arr.size(); j++)
        {
            if(i==j)
                continue;
            int u = 0;
            stringstream ss(arr[i] + arr[j]);
            ss >> u;
            brr.push_back(u);
        }
    }
    sort(brr.begin(), brr.end());
    cout << brr[2] << endl;
    return oOvOo;
}