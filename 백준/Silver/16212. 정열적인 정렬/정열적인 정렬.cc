#include<iostream>
#include<algorithm>
#pragma warning(disable:4996)
using namespace std;

int main()
{
	int n;
	scanf("%d", &n);
	int * arr = new int[n];
	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);
	sort(arr, arr + n);
	for (int i = 0; i < n; i++)
		printf("%d ", arr[i]);
}