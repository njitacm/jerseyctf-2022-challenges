#include <stdio.h>

int main()
{
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    puts("Man this would be really cool if this were a flag.");
    puts("Wouldn't this be nice if it were a flag?");
    puts("Tragic.");
}
