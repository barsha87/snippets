#include <iostream>
#include<conio.h>
int i;
using namespace std;
class heapsort
{
public:void sort(int a[],int n);
void adjust(int a[],int i,int n);
void heapify(int a[],int n);
void display(int a[],int n);
};
void heapsort::display(int a[],int n)
{
     int i=0;
     cout<<endl;
     for(i=1;i<=n;++i)
cout<<a[i]<<"       ";
}
void heapsort::sort(int a[],int n)
{
int temp;
heapify(a,n);
for(i=n;i>=2;i--)
{
                 cout<<endl;
                 display(a,n);
temp=a[1];
a[1]=a[i];
a[i]=temp;
adjust(a,1,i-1);
}
}
void heapsort::adjust(int a[],int i,int n)
{
int j,item;
j=2*i;
item=a[i];
while(j<=n)
{
if((j<n)&&(a[j]<=a[j+1]))
j=j+1;
if(item>=a[j])
break;
a[j/2]=a[j];
j=2*j;
}
a[j/2]=item;
}
void heapsort::heapify(int a[],int n)
{
for(i=n/2;i>=1;--i)
{
                   adjust(a,i,n);
}
}
int main()
{
int i;
int a[20];
int n;
heapsort obj;
cout<<"enter no of elements"<<endl;
cin>>n;
cout<<"enter elements"<<endl;
for(i=1;i<=n;++i)
{
cin>>a[i];
}
obj.sort(a,n);
cout<<"the sorted array"<<endl;
for(i=1;i<=n;++i)
cout<<a[i]<<"       ";
getch();
}


