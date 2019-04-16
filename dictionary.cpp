#include<iostream.h>
#include<conio.h>

main()
{
      char a[10][10],search[10],temp[10];
      int i,j,flag=0,ch;
      
      cout<<"Enter any 10 names \n";
      
      for(i=0;i<10;i++)
      cin>>a[i];
      
      
      for(i=0;i<10;i++)
      {
                       if(strcmp(a[i],a[i+1])>0)
                       {
                                                 
                         strcpy(temp,a[i]);
                         strcpy(a[i],a[i+1]);
                         strcpy(a[i+1],temp);
                                                 
                       }
      }
      
      for(i=0;i<10;i++)
      cout<<endl<<a[i];
     
      cout<<endl;
      do
      {
      cout<<"\nEnter the string you want to search  ";
      cin>>search;
      
      for(i=0;i<10;i++)
      {
      if(strcmp(a[i],search)==0)
       {
        flag=1;
        break;
       }
      }
      
      if(flag==1)
      cout<<"NAME FOUND AT "<<i+1<<"location"<<"\n";
      else 
      cout<<"NAME NOT FOUND\n";
      
      cout<<"PRESS O TO EXIT AND 1 TO CONTINUE  ";
      cin>>ch;
      cout<<endl;
      
      }while(ch!=0);
      
      getch();

}
