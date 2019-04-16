#include <string.h>
#include <stdio.h>

/*Assumptions : Given full name of person (from linked in) and company email id
Output of the program : max score obtained when the name is validated against the first part of the email id.
(Also returns an array of likely scores arranged in descending order)
*/

//removes spl characters from the given string and converts it to lowercase
void removeSpl(char  * str1) {
    int i=0, j=0;
    while(i<=strlen(str1)){
        if((str1[i]>='a' && str1[i]<='z') || (str1[i]>='A' && str1[i]<='Z')){
            str1[j] = str1[i];
            if(str1[j]>='A' && str1[j]<='Z')
                str1[j]+=32;
            i++;j++;
        }
        else i++;
    }
    str1[j]='\0';
}

//concatenates a string and a character
void concat(char * res, char x) {
     int len=strlen(res);
     res[len]=x;
     res[len+1]='\0';
}

//returns minimum of 2 numbers
int min(int a,int b)
{
    return (a<b?a:b);
}

//finds the levenshtein's distance between two given strings
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

//compares the name (13 standardised forms of the name) and the first part of the email using distance and generates score
int nameCmp(char * fullname, char * email)
{
    int score[13],i,j,k,t;
    char name[13][100], tmp [100], fname[100], mname[100], lname[100], userid[50];

    for(j=strlen(fullname)-1, k=0;fullname[j]!=' ' && j>=0;j--, k++)
        lname[k]=fullname[j];
        lname[k]='\0';
        strrev(lname);
    for(i=0;fullname[i]!=' ' && i<strlen(fullname)-k;i++)
        fname[i]=fullname[i];
        fname[i]='\0';
    for(t=i,k=0;t<=j;t++,k++)
        mname[k]=fullname[t];
        mname[k]='\0';
    for(i=0;email[i]!='@' && i<strlen(email);i++)
        userid[i]=email[i];
        userid[i]='\0';

    removeSpl(fname);
    removeSpl(lname);
    removeSpl(mname);
    removeSpl(userid);

    strcpy(name[0],fname);
    strcat(name[0],lname);

    strcpy(name[1],fname);
    strcat(name[1],mname);
    strcat(name[1],lname);

    strcpy(name[2],lname);
    strcat(name[2],fname);

    strcpy(name[3],lname);
    strcat(name[3],fname);
    strcat(name[3],mname);

    strcpy(name[4],mname);
    strcat(name[4],lname);
    strcat(name[4],fname);

    strcpy(name[5],fname);
    concat(name[5],lname[0]);

    strcpy(name[6],fname);
    concat(name[6],mname[0]);
    concat(name[6],lname[0]);

    strcpy(name[7],"");
    concat(name[7],lname[0]);
    strcat(name[7],fname);

    strcpy(name[8],"");
    concat(name[8],mname[0]);
    concat(name[8],lname[0]);
    strcat(name[8],fname);

    strcpy(name[9],lname);
    concat(name[9],fname[0]);

    strcpy(name[10],lname);
    concat(name[10],fname[0]);
    concat(name[10],mname[0]);

    strcpy(name[11],"");
    concat(name[11],fname[0]);
    strcat(name[11],lname);

    strcpy(name[12],"");
    concat(name[12],fname[0]);
    concat(name[12],mname[0]);
    strcat(name[12],lname);

    int u= strlen(userid);
    for (i=0;i<13;i++) {
        score[i]=distance(name[i],userid);
        int n= strlen(name[i]);
        int l= n>u?n:u;
        score[i]=((l-score[i])*100)/l;
    }
    for (i=0;i<13;i++){
        for(j=i+1;j<13;j++) {
            if(score[i]<score[j]){
                 t=score[i];
                 score[i]=score[j];
                 score[j]=t;
                 strcpy(tmp, name[i]);
                 strcpy(name[i],name[j]);
                 strcpy(name[j],tmp);
            }
        }
    }
    //Note to self: do not print duplicate array elements (case when there's no middlename etc.)
    for(i=0;i<13;i++) {
        printf("\n%s : %d", name[i],score[i]);
    }
    return score[0];
}

//dummy main() function
int main ()
{
    char fullname[100], email[100];
    printf("Enter name: ");
    gets(fullname);
    printf("Enter email: ");
    gets(email);
    int score = nameCmp(fullname, email);
    printf("\n\nMax score is: %d\n", score);
    return 0;
}
