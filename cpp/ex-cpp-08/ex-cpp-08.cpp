// g++ -std=c++20 ex-cpp-08.cpp -o build/ex-cpp-08 && ./build/ex-cpp-08
// -----task-source:-ai-generated------
// Zadanie 8: Zamiana wartości
// Napisz program, który wczytuje dwie liczby, wyświetla je, a następnie
// zamienia ich wartości miejscami i wyświetla ponownie.
#include <iostream>

int main() {
  int first;
  int second;
  std::cout << "Give me two numbers and I'm gonna change their places (not "
               "sure why would I do it).\nFirst: ";
  std::cin >> first;
  std::cout << "Second: ";
  std::cin >> second;
  std::cout << "Here are your numbers:\n" << first << second << std::endl;
  std::cout << "And here with their places CHANGED:\n" << second << first;
  return 0;
}
// ----------- Future Tips: -----------
// Some weird exercise idea
