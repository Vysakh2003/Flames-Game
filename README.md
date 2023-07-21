# Flames-Python

The project appears to be a simple implementation of the "FLAMES" game, a fun game often played by people to predict the relationship between two individuals. The game uses the acronym "FLAMES," where each letter represents a different type of relationship: Friends, Lovers, Affectionate, Marriage, Enemies, and Siblings.

How it is computed:

  -✔️ The code first takes the user's input, processes the names to prepare them for further computation.

  -✔️ It then cancels the common letters between the two names and calculates the count of dissimilar letters (c).

  -✔️ A circular doubly linked list is created to represent the FLAMES pattern.

  -✔️ The program removes nodes from the circular doubly linked list based on the value of c, effectively counting and removing nodes until only one node remains.

  -✔️ The remaining letter determines the relationship outcome, and the corresponding message is printed.

Overall, the computation involves string processing, character cancellation, circular doubly linked list manipulation, and conditional checks to determine the relationship outcome.
