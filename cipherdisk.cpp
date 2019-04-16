#include <iostream>
#include <string.h>
#include <math.h>
using namespace std;

int main()
{
	int t,n,i,d,a[200];
	char str[200];
    cin>>t;
    getchar();
    while(t--) {
    	gets(str);
    	a[0]=str[0]-97;
    	for(i=1;i<strlen(str);i++) {
    		d=str[i]-str[i-1];
    		if(abs(d)<=26-abs(d))
    			a[i]=d;
    		else
    			a[i]=abs(d)-26;
    		while(a[i]<-12 ||a[i]>13) {
    			if(a[i]<-12)
    				a[i]=a[i]+26;
    			else if(a[i]>13)
    				a[i]=a[i]-26;
    		}
    	}
    	for(i=0;i<strlen(str);i++) {
    		cout<<a[i]<<" ";
    	}
    	cout<<"\n";
    }
    return 0;
}

