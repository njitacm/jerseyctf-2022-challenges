#include <stdio.h>


void a() {
    puts("jctf{NIL}");
}

void b() {
    puts("nil buster");
}

int main(int argc, char* argv[]) {

    int i;

    char* flag = "patches-ohoulihan";
    char* what = "if-you-can-dodge-a-wrench-you-can-dodge-a-ball";

    for(i = 0; i < 23; i++){
        if( i >= 30) {
            a();
        } 
        b();
    
    }

    return 0;
}