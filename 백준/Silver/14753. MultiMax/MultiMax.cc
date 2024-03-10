#include<iostream>
#include<algorithm>
#include<cstring>
#pragma warning(disable:4996)
using namespace std;

int f(int arr[], int n);

int main()
{
	int n;
	scanf("%d", &n);
	int * arr = new int[n];
	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);
	sort(arr, arr + n, greater<int>());

	printf("%d", f(arr, n));
	delete[] arr;
}

int f(int arr[], int n)
{
	int a = arr[0] * arr[1];
	int b = arr[n - 1] * arr[n - 2];
	int c = arr[0] * arr[1] * arr[2];
	int d = arr[0] * arr[n - 1] * arr[n - 2];
	return max({ a,b,c,d });
}