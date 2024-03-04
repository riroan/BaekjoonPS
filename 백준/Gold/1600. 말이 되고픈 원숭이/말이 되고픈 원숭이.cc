/**
 *    author:  riroan
 *    created:  2024.03.05 01:51:27
 **/
#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
const int oOvOo = 0;
using namespace std;

signed main()
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);
	int k;
	cin >> k;
	k++;
	int n, m;
	cin >> m >> n;
	vector<vector<int>> arr(n, vector<int>(m));
	for (auto &i : arr)
		for (auto &j : i)
			cin >> j;
	auto check = [&](int x, int y)
	{
		return 0 <= x && x < n && 0 <= y && y < m;
	};
	auto get = [&](int x, int y, int k)
	{
		return k * n * m + x * m + y;
	};
	vector<vector<pair<int, int>>> g(n * m * k);
	for (int x = 0; x < n; x++)
	{
		for (int y = 0; y < m; y++)
		{
			for (int z = 0; z < k; z++)
			{
				if (z < k - 1)
				{
					for (auto [dx, dy] : vector<pair<int, int>>({{-2, -1}, {-2, 1}, {-1, -2}, {-1, 2}, {1, -2}, {1, 2}, {2, -1}, {2, 1}}))
					{
						int tx = x + dx, ty = y + dy;
						if (!check(tx, ty))
							continue;
						if (arr[tx][ty])
							continue;
						int cur = get(x, y, z);
						int nxt = get(tx, ty, z + 1);
						g[cur].push_back({nxt, 1LL});
					}
				}
				for (auto [dx, dy] : vector<pair<int, int>>({{-1, 0}, {1, 0}, {0, -1}, {0, 1}}))
				{
					int tx = x + dx, ty = y + dy;
					if (!check(tx, ty))
						continue;
					if (arr[tx][ty])
						continue;
					int cur = get(x, y, z);
					int nxt = get(tx, ty, z);
					g[cur].push_back({nxt, 1LL});
				}
			}
		}
	}
	auto dijkstra = [&](int start)
	{
		int sz = n * m * k;
		vector<int> distances(sz + 1, numeric_limits<int>::max());
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
			for (auto new_destination : g[current_destination])
			{
				auto new_distance = new_destination.second;
				auto destination = new_destination.first;
				auto distance = current_distance + new_distance;
				if (distance < distances[destination])
				{
					distances[destination] = distance;
					q.push({-distance, destination});
				}
			}
		}
		return distances;
	};
	auto d = dijkstra(0);
	int mi = numeric_limits<int>::max();
	for (int i = n * m - 1; i < n * m * k; i += n * m)
		mi = min(mi, d[i]);
	if (mi == numeric_limits<int>::max())
		cout << -1;
	else
		cout << mi;

	return oOvOo;
}
