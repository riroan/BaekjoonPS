#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
#define int long long
const int oOvOo = 0;
using ll = long long;
using namespace std;

signed main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<vector<pair<int, int>>> arr(n);
    while (m--)
    {
        int a, b, c;
        cin >> a >> b >> c;
        a--;
        b--;
        arr[a].push_back({b, c});
    }
    int s, e;
    cin >> s >> e;
    s--;
    e--;
    vector<int> parent(n, -1);
    auto dijkstra = [&](int start)
    {
        vector<ll> distances(n + 1, numeric_limits<ll>::max());
        distances[start] = 0;
        priority_queue<pair<int, int>> q;
        q.push({distances[start], start});
        while (!q.empty())
        {
            auto current_distance = -q.top().first;
            auto current_destination = q.top().second;
            q.pop();
            if (distances[current_destination] < current_distance)
                continue;
            for (auto new_destination : arr[current_destination])
            {
                auto new_distance = new_destination.second;
                auto destination = new_destination.first;
                auto distance = current_distance + new_distance;
                if (distance < distances[destination])
                {
                    parent[destination] = current_destination;
                    distances[destination] = distance;
                    q.push({-distance, destination});
                }
            }
        }
        return distances;
    };
    auto dist = dijkstra(s);
    cout << dist[e] << endl;
    vector<int> answer({e});
    while (s != e)
    {
        e = parent[e];
        answer.push_back(e);
    }
    cout << answer.size() << endl;
    reverse(answer.begin(), answer.end());
    for(auto i : answer)
        cout << i+1 << " ";

    return oOvOo;
}