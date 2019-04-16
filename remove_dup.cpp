#include<iostream>
using namespace std;

int main() {
	int n,a[100],b[100],i,j,count=1, flag=0;
	cout<<"Enter n: ";
	cin>>n;
	cout<<"Enter array:\n";
	for(i=0; i<n; i++){
		cin>>a[i];
	}
	b[0]=a[0];
	for(i=1;i<n;i++){
		flag=0;
		for(j=0;j<count;j++){
			if(a[i]==b[j]){
				flag++;
				break;
			}
		}
		if(flag==0){
			b[count]=a[i];
			count++;
		}
	}
	cout<<"\nArray after removing duplicates:";
	for(i=0;i<count;i++)
		cout<<b[i]<<" ";
	return 0;
}
