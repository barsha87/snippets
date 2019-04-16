# include <stdio.h>
# include <string.h>

extern "C"
{
void func(char n1[],char n2[])
{
char n[2][30];
strcpy(n[0],n1);
strcpy(n[1],n2);
printf("%s\n%s",n[0],n[1]);
}
}