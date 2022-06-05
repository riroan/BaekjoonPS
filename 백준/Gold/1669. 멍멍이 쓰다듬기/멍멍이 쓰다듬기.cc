#include <iostream>
#include<cstring>
#include<cstdlib>
#include<cstdbool>
using namespace std;
#pragma warning(disable:4996)

int main()
{
	int T;
		long x, y;

		scanf("%ld %ld", &x, &y);
		long r = y - x;
		int cnt = 0;
		bool flag = false;
		long exp = 1;
		while (r > 0)
		{
			r -= exp;
			flag = !flag;
			cnt++;
			if (!flag)
				exp++;
		}
		printf("%d\n", cnt);
}