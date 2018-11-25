#include <stdio.h>
#include "error_strings.h"

int main( void )
{
    int err = DoSomething();
    printf( "%s\n", errorStrings[err] );
}
