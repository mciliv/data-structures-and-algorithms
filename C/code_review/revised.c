#include <stdio.h>
#include <string.h>

char *GetErrorString ( int x )
{
    static char errorString[21] = "";
    
    switch (x)
    {
        case 0:
            strcpy (errorString, "Success -- No error.");
            break;
        case 2:
            strcpy (errorString, "Overflow!");
            break;
        default:
            strcpy (errorString, "Unknown!");
    }
    
    return errorString;
}

int main ( void )
{
    int err = DoSomething();
    
    printf ("%s\n", GetErrorString ( err ) );
}
