#include <stdio.h>

void printfunc(char *str)
{
    printf(str);
}

int main()
{
    
    char amessage1[] = "no"; /* an array */
    char amessage2[] = "no"; /* an array */
    char *pmessage1 = "no"; /* a pointer */
    char *pmessage2 = "no"; /* a pointer */

    printf("amessage1: %p\n", amessage1);
    printf("amessage2: %s\n", amessage2);
    printf("pmessage1: %p\n", pmessage1);
    printf("pmessage2: %s\n", pmessage2);
    
    printfunc(&"hello");
}


