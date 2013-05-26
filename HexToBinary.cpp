//
// HexToBinary.cpp
//
// Mark Cerqueira
// Copyright 2010 Smule, Inc. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, char* argv[]) 
{
    // check number of arguments
    if ( argc != 3 ) 
    {
        cout << "usage: HexToBinary input.txt output.txt" << endl;
        return 0;
    }
    
    FILE *input= fopen( argv[1], "r+" );
    FILE *output = fopen( argv[2], "w+" );

    // check if input file was opened
    if( input == NULL )
    {
        cout << "unable to open file " << argv[1] << endl;
        return 0;
    }
    
    // check if output file was created
    if ( output == NULL )
    {
        cout << "error writing to file " << argv[2] << endl;
        return 0;
    }
    
    char info[3];
    int n;	

    while( feof(input) == 0 )
    {
       if( fread(info, sizeof(info) - 1, 1, input) != 0 )
       {
           info[2] = '\0';
           
           sscanf(info, "%x", &n);
           
           fwrite(&n, 1, 1, output);
       }
    }

    
    fclose( output );
    fclose( input );
    
    return 1;
}
