#include<iostream.h>
#include<conio.h>
main()
{     int n,i,j,k,temp,min_loc;
      
      cout<<"enter the size of array\n";
      cin>>n;
      
      int a[n];
      
      cout<<"\n enter the numbers\n";
      for(i=0;i<n;i++)
      cin>>a[i];
     
    
for(i=0; i<n-1; i++)

	{
        min_loc = i;
        for(int j=i+1; j<n; j++)
        {
            if(a[min_loc]>a[j])
            min_loc = j;
        }
        
		temp = a[i];
        a[i] = a[min_loc];
        a[min_loc] = temp;
        cout<<endl;
        for(int k=0;k<n;k++)
       cout<<a[k]<<endl;       

	}


     
     cout<<"\nThe sorted list is \n";
     for(i=0;i<n;i++)
       cout<<a[i]<<endl;

getch();
}
      
