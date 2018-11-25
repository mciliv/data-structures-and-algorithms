// My code review

// #include <stdio.h> // Remember to include the contents of the standard header 'stdio.h' since you're printing to standard output.


char *GetErrorString( int x )
{
    char errorString[20]; // Should be of size 21 since '\0' needs to be stored at the end of the 20 character long string, "Success -- No error.".
                          // However, defining errorString like this won't allow you to assign 'errorString'
                          // Making this 'char *errorString' makes this a pointer seems to better fit what you want to do because you assign the string value later,
                          // you don't change the string value, and you'll be passing it


    switch ( x ) // I switching this 'switch' statement to the array method shown in q1_morgan.c.
    {
        case 0:
            errorString = "Success -- No error.";
            break;
        case 2:
            errorString = "Overflow!";
            break;
            
        // Add a catch all
    }

    errorString[19] = 0; //The last thing in the string should be the null character, '\0', not 0.
                         // C will automitcally do this since you assigned the character array to a string literal, so this line isn't necessary anyways.
    
    return errorString;
}

void main( void ) // Should be 'int' return a type instead of type 'void', 'main' defaults to returning 0, meaning normal exit of program.
{
    int err = DoSomething();
    if ( err ) // When the variable 'err' gets the integer value 0, the body of the 'if' statement will not execute.
               // Therefore, the case that 'x' is 0 in the switch statement will never be executed.
               // Depending on your intention, this statement should not be a conditional or case '0' of the 'switch' statement in GetErrorString is extraneous.
    {
        printf( "%s\n", GetErrorString( err ) );
    }
}
