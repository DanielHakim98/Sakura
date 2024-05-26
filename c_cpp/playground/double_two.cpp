#include <ios>
#include <iostream>
#include <limits>

double get_input() {
  double in;
  std::cout << "Enter an integer: ";
  std::cin >> in;
  return in;
}

int main() {
  double user_input = get_input();

  while (std::cin.fail()) {
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cout << "Input is not a number. Please try again.\n";
    user_input = get_input();
  }

  std::cout << "Double that number is: " << user_input * 2 << '\n';
  return 0;
}
