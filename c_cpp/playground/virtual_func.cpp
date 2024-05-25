#include <iostream>
#include <ostream>
class Animal {
public:
  virtual void eat() { std::cout << "I'm eating generic food." << std::endl; }
};

class Cat : public Animal {
public:
  void eat() { std::cout << "I'm eating a rat." << std::endl; }
  void purr() { std::cout << "Cat is purring" << std::endl; }
};

void func(Animal *xyz) { xyz->eat(); }

int main(int argc, char *argv[]) {
  Animal *animal = new Animal;
  Animal *cat = new Cat;

  func(animal);
  func(cat);

  Cat *real_cat = dynamic_cast<Cat *>(cat);
  if (real_cat != nullptr) {
    real_cat->purr();
  }

  delete animal;
  delete cat;

  return 0;
}
