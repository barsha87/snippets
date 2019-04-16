#include <iostream>
using namespace std;

void bubble (int a[], int n) {
	int i, j, k, tmp, not_sorted=1;
	for (i=n-1;i>=0 && not_sorted;i--) {
		not_sorted= 0;
		for (j=0;j<i;j++) {
			if(a[j]>a[j+1]) {
				tmp=a[j];
				a[j]=a[j+1];
				a[j+1]=tmp;
				not_sorted=1;
			}
		//just printing	
		for(k=0;k<n;k++) {
			cout<<a[k]<<"  ";
		}
		cout<<"\n";
		}
	cout <<"PASS complete\n";
	}	
}

int main () {
	int a[] = {25, 13, 12, 5, 1, 0};
	int k;
	bubble (a, 6);
	cout<<"\n sorted:\n";
	for(k=0;k<6;k++) {
			cout<<a[k]<<"  ";
		}
}

/*{7,  3,  21,  25,  11,  19};
{25, 13, 12, 5, 1, 0};
{4,4,4,5,5,5}
{7,8,9,10,11,12}

/*
3  7  21  25  11  19
3  7  21  25  11  19
3  7  21  11  25  19
3  7  21  11  19  25
PASS complete
3  7  21  11  19  25
3  7  11  21  19  25
3  7  11  19  21  25
3  7  11  19  21  25
PASS complete
3  7  11  19  21  25
3  7  11  19  21  25
3  7  11  19  21  25
PASS complete
3  7  11  19  21  25
3  7  11  19  21  25
PASS complete
3  7  11  19  21  25
PASS complete

 sorted:
3  7  11  19  21  25
*/
