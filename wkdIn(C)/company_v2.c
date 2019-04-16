#include <string.h>
#include <stdio.h>

/*Assumptions : Given name of company (from linked in) and company email id and relevant google search results.
Output of the program : max score obtained when the company name is validated against the second part of the email id.
*/

extern "C"
{

//removes spl characters from the given string and converts it to lowercase
void removeSpl(char  * str1) {
    int i=0, j=0;
    while(i<=strlen(str1)){
        if((str1[i]>='a' && str1[i]<='z') || (str1[i]>='A' && str1[i]<='Z')|| str1[i]==' ' || str1[i]=='.'){
            str1[j] = str1[i];
            if(str1[j]>='A' && str1[j]<='Z')
                str1[j]+=32;
            i++;j++;
        }
        else i++;
    }
    str1[j]='\0';
}

//returns minimum of 2 numbers
 int min(int a,int b)
{
    return (a<b?a:b);
}

//levensthein's distnce between two strings
int distance (char * word1, char * word2)
{
    int i;
    int len1 = strlen(word1);
    int len2 = strlen(word2);
    int matrix[len1 + 1][len2 + 1];
    for (i = 0; i <= len1; i++)
        matrix[i][0] = i;
    for (i = 0; i <= len2; i++)
        matrix[0][i] = i;

    for (i = 1; i <= len1; i++){
        int j;
        char c1;
        c1 = word1[i-1];
        for (j = 1; j <= len2; j++) {
            char c2;
            c2 = word2[j-1];
            if (c1 == c2)
                matrix[i][j] = matrix[i-1][j-1];
            else
                matrix[i][j] = min(min(matrix[i-1][j],matrix[i][j-1]), matrix[i-1][j-1])+1;
        }
    }
    return matrix[len1][len2];
}

//returns score based on scoring algorithm
/*
x: case identifier
st1: string to be compared
st2: array of 3 strings obtained from google search
*/
int companyCmp(int x, char * st1, char *st2[100])
{
    int score;
    removeSpl(st1);
    removeSpl(st2[0]);
    removeSpl(st2[1]);
    removeSpl(st2[2]);
    switch (x) {
        case 1: //compare string with array of strings and return score accordingly
                if (strstr(st1, st2[0]) || strstr(st2[0],st1))
                     return 100;
                else if (strstr(st1,st2[1]) || strstr(st2[1],st1))
                     return 70;
                else if (strstr(st1,st2[2]) || strstr (st2[1],st1))
                     return 50;
                else return 0;
        case 2: //find Lev dist between 1st search result and string and return score
                score = distance(st1, st2[0]);
                int n= strlen(st1);
                int u= strlen(st2[0]);
                int l= n>u?n:u;

                score=((l-score)*20)/l;
                return score;
    }
}

//Called by wrapper program, compares company name with 1st three google search results
/*
str1 :Array of company domains; last element is company name
l1: length of str1
str2 : array of company names; last element is email id
l2: length of str2
*/
void start_here(int l1, char* str1[100], int l2, char* str2[100])
{
    char cmpname[100], email[100], domain[100];
    int i, k, score=0, tmp=0;

    strcpy(cmpname, str1[l1-1]);
    strcpy(email, str2[l2-1]);

    for(i=strlen(email)-1,k=0;email[i]!='@' && i>=0;i--,k++)
        domain[k]=email[i];
    domain[k]='\0';
    strrev(domain);

    score = companyCmp(1, domain, str1);
    if (score !=100) {
        tmp = companyCmp(1, cmpname, str2);
        score /=2;
        if(tmp != 0)
            score += (tmp/2);
        else {
            tmp = companyCmp(2, cmpname, str2);
            score += tmp;
        }
    }
    printf("\nScore is: %d\n", score);
}

//dummy main() function
/*int main()
{
    start_here();
}
*/
}

