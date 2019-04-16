//merge sorted arrays into one sorted array

#include<iostream>
using namespace std;

void mergesort(int*a, int*b, int*c, int l1, int l2){
	int *n1, *n2;
	n1=a+l1;
	n2=b+l2;
	while(a<n1 || b<n2) {
		while (a<n1 && (*a < *b || b>=n2)){
			*c=*a;
			a++;c++;
		}
		while (b<n2 && (*b < *a || a>=n1)){
			*c=*b;
			b++;c++;
		}
	}
}

int main(){
	int a[100], b[100], c[200], l1, l2, i;
	cout<<"\nEnter number of elements in 1st array: ";
	cin>>l1;
	cout<<"\nEnter 1st array\n";
	for(i=0; i<l1;i++)
		cin>>a[i];
	cout<<"\nEnter number of elements in 2nd array: ";
	cin>>l2;
	cout<<"\nEnter 2nd array\n";
	for(i=0; i<l2;i++)
		cin>>b[i];
	mergesort(a,b,c,l1,l2);
	cout<<"\nMerged array:\n";
	for(i=0; i<l1+l2;i++)
		cout<<c[i]<<" ";
	return 0;
}
