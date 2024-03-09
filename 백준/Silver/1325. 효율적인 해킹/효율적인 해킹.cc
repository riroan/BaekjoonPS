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
	int n, m;
	cin >> n >> m;
	vector<vector<int>> g(n);
	for (int i = 0; i < m; i++)
	{
		int a, b;
		cin >> a >> b;
		g[b - 1].push_back(a - 1);
	}
	vector<int> ans, l(n, 0), v(n, 0);
	int cnt = 0;
	for (int i = 0; i < n; i++)
	{
		v = vector<int>(n, 0);
		cnt = 0;
		queue<int> q;
		q.push(i);
		v[i] = 1;
		while (!q.empty())
		{
			int x = q.front();
			q.pop();
			for (auto j : g[x])
			{
				if(v[j])
					continue;
				cnt++;
				v[j] = 1;
				q.push(j);
			}
		}
		l[i] = cnt;
	}
	int mm = 0;
	for (auto i : l)
		mm = max(mm, i);
	for (int i = 0; i < n; i++)
		if (l[i] == mm)
			ans.push_back(i + 1);
	for (auto i : ans)
		cout << i << " ";
	return oOvOo;
}
