
#include <iostream>

int main() 
{
    std::string s;
    while( getline( std::cin, s ) ) {
        std::cout << s << std::endl;
    }
}