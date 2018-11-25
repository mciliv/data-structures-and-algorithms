//
//  q1_play.c
//  
//
//  Created by Morgan Ciliv on 7/19/18.
//

#include <stdio.h>
void swap(int *m, int *n)
{
    int temp = *m;
    *m = *n;
    *n = temp;
}

int main( void )
{
    char *word[6];
    *word = "hello\0";
    printf("%s\n", *word);
//
//    printf("%p\n", word);
//    printf("%p\n", *word);
//    printf("%c\n", **word);
//    printf("%c\n", *(*word + 1));

    int a = 0;
    int b = 1;
    int *x = &a;
    int *y = &b;
    
    printf("X contains: %d\n", *x);
    printf("Y contains: %d\n", *y);
    swap(x, y);
    printf("X now contains: %d\n", *x);
    printf("Y now contains: %d\n", *y);
}
