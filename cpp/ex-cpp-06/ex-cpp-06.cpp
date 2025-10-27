// g++ -std=c++20 ex-cpp-06.cpp -o build/ex-cpp-06 && ./build/ex-cpp-06
// -----task-source:-ai-generated------
// Zadanie 6: Obliczanie pola prostokąta
// Napisz program, który wczytuje długość i szerokość prostokąta, a następnie
// oblicza i wyświetla jego pole.
#include <iostream>

int main() {
  int height;
  int length;
  std::cout << "Give me length and hight of a rectangle and I'll give you it's "
               "area.\n";
  std::cout << "Hight:\n";
  std::cin >> height;
  std::cout << "Length:\n";
  std::cin >> length;
  int area = height * length;
  std::cout << "The area is: " << area << std::endl;
  return 0;
}
// ----------- Future Tips: -----------
