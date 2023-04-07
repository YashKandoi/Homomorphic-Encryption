#include <stdio.h>
int main()
{

    printf("enter number of qns\n");
    int n;
    scanf("%d", &n);
    // printf("%d\n", n);
    char arr1[n];
    char arr2[n];
    printf("Enter key\n");
    int i = 0;
    // for (i = 0; i < n; i++)
    // {
        scanf("%s", arr1);
    // }
    // for (i = 0; i < n; i++)
    // {
    //     printf("%c\n", arr1[i]);
    // }
    // printf("%s",arr1);

    // printf("%d\n", i);
    printf("Enter attempt\n");
    // for (i = 0; i < n; i++)
    // {
        scanf("%s", arr2);
    // }
    // for (i = 0; i < n; i++)
    // {
    //     printf("%c\n", arr2[i]);
    // }

    int marks = 0;
    for (i = 0; i < n; i++)
    {
        if (arr1[i] == arr2[i])
        {
            marks++;
        }
    }
    printf("the marks obtained are %d out of %d\n", marks, n);
}