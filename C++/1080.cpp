#include <iostream>


int main()
{
    int values[100];


    for (int i = 0; i < 100; i++ )
    {
        std::cin >> values[i];
    }

    int precessor = 0;
    int pos = 0;
    for (int i = 0; i < 100; i++)
    {
        if (values[i] > precessor)
        {
            precessor = values[i];
            pos = i + 1;
        }
    }

    std::cout << precessor << std::endl;
    std::cout << pos << std::endl;

    


}
