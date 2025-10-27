// g++ -std=c++20 ex-cpp-07.cpp -o build/ex-cpp-07 && ./build/ex-cpp-07
// -----task-source:-ai-generated------
// Zadanie 7: Średnia trzech liczb
// Napisz program, który wczytuje trzy liczby i oblicza ich średnią
// arytmetyczną.
#include <iostream>

int main() {
  int first;
  int second;
  int third;
  std::cout << "Give me three numbers and I'll calculate the mean.\nFirst:"
            << std::endl;
  std::cin >> first;
  std::cout << "Second:\n";
  std::cin >> second;
  std::cout << "Third:\n";
  std::cin >> third;
  int mean = (first + second + third) / 3;
  std::cout << "The mean is " << mean << std::endl;
  return 0;
}
// ----------- Future Tips: -----------
