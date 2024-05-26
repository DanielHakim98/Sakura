#include <iostream>

// let's compare between two variables
// instantiated 'x_init' 'x_uninit'
int main() {
  int x_uninit;
  std::cout << x_uninit << '\n';

  int x_init{};
  std::cout << x_init << '\n';
  return 0;
}
