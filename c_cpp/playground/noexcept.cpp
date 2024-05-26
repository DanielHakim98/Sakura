
#include <iostream>
#include <stdexcept>
class Example {
public:
  // no exception function
  void safeFunction() noexcept {
    std::cout << "This function is safe and will not throw exceptions. \n";
  }

  // may throw exception function
  void riskyFunction() noexcept(false) {
    std::cout << "This function may throw an exception. \n";
    throw std::runtime_error("An error occured in riskyFunction.");
  }

  // regular function
  void normalFunction() {
    std::cout << "This is normal function without noexcept specification. \n";
  }
};

int main() {
  Example anObject;

  anObject.safeFunction();
  try {
    anObject.riskyFunction();
  } catch (const std::exception &e) {
    std::cout << "Caught exception: " << e.what() << "\n";
  }

  // Checking noexcept properties
  std::cout << std::boolalpha;
  std::cout << "Is safeFunction noexcept? " << noexcept(anObject.safeFunction())
            << "\n";
  std::cout << "Is riskyFunction noexcept? "
            << noexcept(anObject.riskyFunction()) << "\n";
  std::cout << "Is normalFunction noexcept? "
            << noexcept(anObject.normalFunction()) << "\n";

  return 0;
}
