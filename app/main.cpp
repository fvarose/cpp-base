#include <iostream>

#include <dummy.hpp>

int main()         {
  std::cout << "app::main()\n";

  dummy d{"name"};
  std::cout << is_dummy(d);
}