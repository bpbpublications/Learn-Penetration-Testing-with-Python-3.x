#include <stdio.h>
#include <string.h>

void func(char *password)
{
    char buf[50];
    strcpy(buf, password);
    printf("Exploit %s\n", buf);
}

int main(int argc, char *argv[])
{
   func(argv[1]);
   return 0;
}
