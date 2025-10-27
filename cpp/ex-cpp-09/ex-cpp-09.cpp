// g++ -std=c++20 ex-cpp-09.cpp -o build/ex-cpp-09 && ./build/ex-cpp-09
// -----task-source:-ai-generated------
// Zadanie 9: Obwód koła
// Napisz program, który wczytuje promień koła i oblicza jego obwód. Użyj
// wartości π = 3.14159.
#include <iostream>
int main() {
  int radius;
  double pi = 3.14159;
  std::cout << "Give me radius of a circle and I'll calculate the circuit.\n";
  std::cin >> radius;
  int circuit = 2 * pi * radius;
  std::cout << "Here is the circuit: " << circuit << std::endl;
  return 0;
}
// ----------- Future Tips: -----------
// pi można ustawić jako stałą:
// const double pi = 3.14159;
