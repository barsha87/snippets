#include<iostream.h>
#include<conio.h>
#include<string.h>

int e=0;

char add(char a,char b);

int main()
{
  char div[80];
  int n,k=0,i,j;
  
  label:
  //input
  cout<<"Enter a binary no.: "<<endl;
  
  gets(div);
  n=strlen(div);
  
  //if input not in binary form
  for(i=0;i<n;i++)
    if(div[i]!='0' && div[i]!='1')
      goto label;
  
  //grouping in sets of two digits
  if(n%2!=0)
  {
    for(i=n-1;i>=0;i--)
      div[i+1]=div[i];
    div[0]='0';
    div[++n]='\0';
   }
   
   char t[n],test[n],q[n/2],p[80];

   //intializing test array
   for(i=0;i<n;i++)
     t[i]=0;
   t[0]='0';
   t[1]='1';
   
   //storing dividend in a dummy array p and t in dummy array test for restoring later
   strcpy(p,div);

   //repeats while no. of quotient bits are less than (div bits)/2
   while(k<n/2)
   {
     strcpy(test,t);

     //finding 1's comp of t 
     for(i=0;i<2*k+2;i++)
          {
          if(t[i]=='0')
             t[i]='1';
          else t[i]='0';
          }

     //finding 2's comp of t
     i=2*k+1;
     while(test[i]!='1')
          {
          t[i]=test[i];
          i--;
          }
     t[i]=test[i];

     //subtracting t from div bits
     for(i=2*k+1;i>=0;i--)
         p[i]=add(div[i],t[i]);
         
     //if subtracted value is negative; restore; quotient bit bcums 0
     if(e==0)
     {
        strcpy(p,div);     
        q[k++]='0';     
     }
     
     //quotient bit bcums 1
     else
     {
         q[k++]='1';
     }       
     
     strcpy(div,p);
     
     //initializing t bits
     t[2*k+1]='1';
     t[2*k]='0';
     i=2*k-1;
     for(j=k-1;j>=0;j--)
       {
       t[i]=q[j];
       i--;
       }
     
     while(i>=0)
     {
       t[i]='0';
       i--;
     }
     
     e=0;
   }
   cout<<"Square root: "<<q<<endl<<"Remainder: "<<div<<endl;
   getch();
   return 0;
}     

char add(char x, char y)
{
     
     if(x=='1' && y=='1')
     {
       if(e==1) 
          return '1';
       else 
          {
          e=1;
          return '0';
          }
     }
     else if(x=='0' && y=='0')
     {
          if(e==1)
            {
            e=0;
            return '1';
            }
          else
            return '0';
     }
     else
     {
        if(e==1)
           return '0';
        else
           return '1';
     }     
     
 }
