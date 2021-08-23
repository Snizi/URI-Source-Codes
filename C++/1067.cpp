#include <iostream>

int main() 
{
    int num = 0;
    
    std::cin >> num;

    for (int i = 1; i <= num; i++)
    {
        if (i % 2 != 0)
        {
            std::cout << i << std::endl;
        }
    }
}
