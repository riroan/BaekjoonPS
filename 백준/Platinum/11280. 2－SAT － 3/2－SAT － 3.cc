#include<bits/stdc++.h>
#define MAX 30000
using namespace std;

int id, d[MAX];
bool finished[MAX];
vector<int> a[MAX];
vector<vector<int>> SCC;
stack<int> s;
int n;

int dfs(int x) {
	d[x] = ++id;
	s.push(x);

	int parent = d[x];
	for (int i = 0; i < a[x].size(); i++) {
		int y = a[x][i];
		if (d[y] == 0) parent = min(parent, dfs(y));
		else if (!finished[y]) parent = min(parent, d[y]);
	}
	if (parent == d[x]) {
		vector<int> scc;
		while (1) {
			int t = s.top();
			s.pop();
			scc.push_back(t);
			finished[t] = true;
			if (t == x) break;
		}
		SCC.push_back(scc);
	}
	return parent;

}
int preprocess(int a) {
	if (a < 0)
		return abs(a) + n - 1;
	return a - 1;
}

int apply_not(int a) {
	return (a + n) % (2 * n);
}

int main() {
	int m;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int x, y;
		cin >> x >> y;
		x = preprocess(x);
		y = preprocess(y);
		a[apply_not(x)].push_back(y);
		a[apply_not(y)].push_back(x);
	}
	for (int i = 0; i < 2 * n; i++)
		if (d[i] == 0)
			dfs(i);
	for (int i = 0; i < SCC.size(); i++)
		sort(SCC[i].begin(), SCC[i].end());
	sort(SCC.begin(), SCC.end());
	bool flag = true;
	for (int i = 0; i < SCC.size(); i++) {
		vector<bool> tt(2 * n, false);
		for (int j = 0; j < SCC[i].size(); j++)
			tt[SCC[i][j]] = true;
		for (int j = 0; j < n; j++)
			if (tt[j] && tt[j + n])
				flag = false;
	}
	cout << (flag ? 1 : 0) << endl;
}