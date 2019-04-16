# include <stdio.h>

int funct(int **x)
{
    int sum = 0;
    int i,j;
    int siz = sizeof(int);

    for(i=0;i<4;++i)
    {
            j = *(x+i);
            sum = sum + j;

    }

    return sum;
}

int main()
{
    int as[2][2] = {{1,2},{3,4}};
    int s;
    s = funct(as);
    printf("%d",s);

    return 0;
}
