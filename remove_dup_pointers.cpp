#include<iostream>
using namespace std;


//Remove dup in the same array

int remove_dup(int *arr, int n) {
	int *ptr, *end = arr+n-1;
	while(arr<=end){
		for(ptr=arr+1;ptr<=end;ptr++){
			if(*arr==*ptr){
				*ptr=*end--;
				n--;
			}
		}
		arr++;
	}
	return n;
}
int main(){
	int n,a[100],i;
	cout<<"Enter n: ";
	cin>>n;
	cout<<"Enter array:\n";
	for(i=0; i<n; i++){
		cin>>a[i];
	}
	int len=remove_dup(a, n);
	cout<<"\nArray after removing duplicates:";
	for(i=0;i<len;i++)
		cout<<a[i]<<" ";
	return 0;
}
