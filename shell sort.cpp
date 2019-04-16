#include<iostream.h>
#include<conio.h>

main()
{     
      int n,i,j,k,temp;
      
      cout<<"enter the size of array\n";
      cin>>n;
      
      int a[n];
      
      cout<<"\n enter the numbers\n";
      for(i=0;i<n;i++)
      cin>>a[i];
      
      for(k=n/2;k>0;k=k/2)
      {
                          for(i=k;i<n;i++)
                          {
                                          temp=a[i];
                                          
                                          for(j=i;j>=k;j=j-k)
                                          
                                          if(temp<a[j-k])
                                          a[j]=a[j-k];
                                          else
                                          break;
                                          
                                          a[j]=temp;
                          }
                           cout<<endl;
                           for(i=0;i<n;i++)
                           cout<<a[i]<<endl;
                           cout<<endl;
                          
      }
                                          
                                          
                                          
      cout<<"\nThe sorted elements are \n";
      for(i=0;i<n;i++)
      cout<<a[i]<<endl;
      getch();
}
