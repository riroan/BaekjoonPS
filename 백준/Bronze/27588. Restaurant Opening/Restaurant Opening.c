/**
 *    author:  riroan
 *    created:  2024.02.22 23:09:31
 **/
#include <stdio.h>

int abs(int a)
{
	return a > 0 ? a : -a;
}

int min(int a, int b)
{
	return a > b ? b : a;
}

int main()
{
	int n, m;
	scanf("%d %d", &n, &m);
	int arr[50][50];
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			scanf("%d", &arr[i][j]);
	int ans = 123456789;
	for (int x = 0; x < n; x++)
	{
		for (int y = 0; y < m; y++)
		{
			int tmp = 0;
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < m; j++)
				{
					tmp += arr[i][j] * (abs(x - i) + abs(y - j));
				}
			}
			ans = min(ans, tmp);
		}
	}
	printf("%d", ans);
}
