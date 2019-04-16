#include<iostream.h>
#include<conio.h>
main()
{     int n,i,j,temp;
      
      cout<<"enter the size of array\n";
      cin>>n;
      
      int a[n];
      
      cout<<"\n enter the numbers\n";
      for(i=0;i<n;i++)
      cin>>a[i];
   
  

      for(i = 1; i < n; i++) 
      {  
            temp=a[i];
            j=i-1;
            while(j>=0)
            {
                       if(a[j]>temp)
                       {
                        a[j+1]=a[j];
                        j--;
                       }
                       else
                        break;
            }
            a[j+1]=temp;
       //cout<<endl;
       //for(int k=0;k<n;k++)
       //cout<<a[k]<<endl;
      }
            
            
            
             cout<<"\nThe sorted elements are \n";
     for(i=0;i<n;i++)
       cout<<a[i]<<endl;

getch();
}
