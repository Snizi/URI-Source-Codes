#include <iostream>


int main()
{

    const char* months[13] = {"fvck", "January", "February", "March", "April", "May", "June" 
                        "August", "September", "October", "November", "December" };

    int num;
    std::cin >> num;

    for (int i = 1; i < 13; i++ )
    {
        if (num == i)
        {
            std::cout << months[i] << std::endl;
        }
    }

