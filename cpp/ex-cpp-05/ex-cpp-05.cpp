// g++ -std=c++20 ex-cpp-05.cpp -o build/ex-cpp-05 && ./build/ex-cpp-05
// -----task-source:-ai-generated------
// Zadanie 5: Kalkulator dwóch liczb
// Napisz program, który wczytuje dwie liczby od użytkownika i wyświetla ich
// sumę.
#include <iostream>

int main() {
  int x;
  int y;
  std::cout << "Give me two numbers, I'll give you their sum :)" << std::endl;
  std::cout << "First:" << std::endl;
  std::cin >> x;
  std::cout << "Second:" << std::endl;
  std::cin >> y;
  int sum = x + y;
  std::cout << "Their sum is: " << sum << std::endl;
  return 0;
}
// ----------- Future Tips: -----------
