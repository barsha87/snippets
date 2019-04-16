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
   
  

      for (i = 1; i < n; i++) 

         {  
             j = i;
             while (j > 0 && a[j - 1] > a[j]) 


            {                  
                 temp = a[j];

                  a[j] = a[j - 1];

                  a[j - 1] = temp;
                  
                  
                 
                  j--;
           }
           }
            
            
            
             cout<<"\nThe sorted elements are \n";
     for(i=0;i<n;i++)
       cout<<a[i]<<endl;

getch();
}
