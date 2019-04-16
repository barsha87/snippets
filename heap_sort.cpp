#include<iostream.h>
#include<conio.h>
int a[50];
void restoreh_down(int,int);
void restoreh_up(int n)
{
     int i,t;
     for(i=n-1;i>0;i--)
         {
             if(a[i]>a[(i-1)/2])
                 {
                 t=a[i];
                 a[i]=a[(i-1)/2];
                 a[(i-1)/2]=t;
                 restoreh_down(i,n);
                 }
             }
     }
     
void restoreh_down(int j,int n)
{
     int i,t;
     i=2*j+1;
     if(i<n)
     {
         if(a[i]<a[i+1] && i+1<n)
             i++;
         if(a[i]>a[(i-1)/2])
             {
             t=a[i];
             a[i]=a[(i-1)/2];
             a[(i-1)/2]=t;
             restoreh_down(i,n);
             }
     }
}
     
     
main()
{
      int i,j,n,temp;
      cout<<"enter no. of elements in array: ";
      cin>>n;
      cout<<"enter elements:\n";
      for(i=0;i<n;i++)
          cin>>a[i];
      restoreh_up(n);
      for(i=0;i<n-1;i++)
      {
              temp=a[0];
              a[0]=a[n-i-1];
              a[n-i-1]=temp;
              restoreh_down(0,n-i-1);
              
      }
      cout<<"\narray after heap sort:\n";
      for(i=0;i<n;i++)
          cout<<a[i]<<"  ";
      getch();
}
