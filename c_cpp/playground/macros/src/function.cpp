#include <iostream>
#define PRINT
void do_something() {
#ifdef PRINT
  std::cout << "Printing!\n";
#endif
#ifndef PRINT
  std::cout << "Not printing!\n";
#endif
}
