#include <stdio.h>

int main () {
   char password[20];

   printf("put a password: ");
   scanf("%s", password);

   printf("Correct %s\n", password);
   printf("Program exited normally");
   return(0);
}