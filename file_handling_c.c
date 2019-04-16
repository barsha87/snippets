#include<stdio.h>
#include<string.h>

void scpy(char d[],char *s,int SIZE)
{
    int i;
    for(i=0;i<=SIZE;++i)
    {
        d[i] = s[i];
    }
}

int main()
{
    FILE * ptr;
    char line[128];
    char title [100];
    char titles[100][25];
    int i=0,j=0, c=0,k=0;
    ptr = fopen("test.txt", "r");

    if(ptr == NULL)
    {

        printf("Open operation failed.");
        return 1;
    }
    while ( fgets ( line, sizeof(line), ptr ) != NULL ) /* read a line */
      { j=0;
        title[0] = strtok(line, ",");
        while(title[j]!= NULL){
            j++;
            title[j] = strtok(NULL, ",");
        }
        //printf("%d\n",j);
      //}
        j--;
        for(i=0;i<j;i++){
            strcpy(titles[c],title[i]);
            c++;
            }
        //printf("%d\n",c);
      }
    for(i=0;i<c;i++){
        puts(titles[i]);
    }
    fclose(ptr);
    return 0;
}
