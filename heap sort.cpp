#include<iostream.h>
#include<conio.h>
void heapify(int ,int );
void heapsort(int ,int );
void adjust(int ,int ,int );

main()
{     int n;
      cout<<"\n Insert the size of the array\n";
      cin>>n;
      
      int a[n];
      for(int i=0;i<n;i++)
      cin>>a[i];
      
      heapify(a,n);
      heapsort(a,n);
      getch();
      
}

void heapsort(int a[],int n)
{           int i,temp;
            
             for(i=n;i>=2;i--)
             {
                     adjust(a,i,n);
                     heapify(a,n);
                     temp=a[1];
                     a[1]=a[i];
                     a[i]=temp;
                     adjust(a,1,i-1);
             }
}

void heapify(int a,int n)
{    int i;
            for(i=n/2;i>=1;i--)
            adjust(a,i,n);
}

void adjust(int a[],int i,int n)
{          int j,item;
             j=2*i;
             item=a[i];
             while(j<=n)
             {
                        if((j<n)&&(a[j]<a[j+1]))
                        j=j+1;
             if(item>=a[j])
             break;
             a[j/2]=a[j];
             j=2*j;
             }
             a[j/2]=item;
}
