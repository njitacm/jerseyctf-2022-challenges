#include <stdio.h>
#include <string.h>
#include <signal.h>
#include <ucontext.h>

static volatile char inp[32];
static const char expected[32] =
    {0x6a, 0x63, 0x39, 0x30, 0x2e, 0x2b, 0x34, 0x4e, 0x4c, 0x1b, 0x4f, 0x2d, 0x5b, 0xb, 0x79, 0x1c, 0x20, 0x7b, 0xa, 0x6b, 0x4f, 0x20, 0x11, 0x72, 0x70, 0x23, 0x63, 0x77, 0x18, 0x3a, 0x6a, 0x5e};
static ucontext_t ctx1, ctx2, ctx_main;

static char stack1[SIGSTKSZ], stack2[SIGSTKSZ];

#define SWP(i1, i2) { \
    int tmp = inp[i1]; \
    inp[i1] = inp[i2]; \
    inp[i2] = tmp; \
}

void func1() {
    for (int i = 6; i < 28; i++) {
        inp[i] ^= 0x37;
        if (i == 16) {
            swapcontext(&ctx1, &ctx2);
        }
    }

    SWP(24, 5)

    for (int i = 3; i < 22; i++) {
        inp[i] ^= inp[i-1];
        if (i == 7) {
            swapcontext(&ctx1, &ctx2);
        }
    }

    SWP(9, 6)

    for (int i = 13; i < 30; i++) {
        SWP(12, i)
        if (i == 21) {
            swapcontext(&ctx1, &ctx2);
        }
    }

    SWP(15, 27)
}

void func2() {
    for (int i = 3; i < 29; i++) {
        SWP(2, i)
        if (i == 11) {
            swapcontext(&ctx2, &ctx1);
        }
    }

    SWP(20, 11)

    for (int i = 12; i < 32; i++) {
        inp[i] ^= inp[i-1];
        if (i == 20) {
            swapcontext(&ctx2, &ctx1);
        }
    }

    SWP(27, 30)

    for (int i = 4; i < 18; i++) {
        inp[i] ^= 0x78;
        if (i == 14) {
            swapcontext(&ctx2, &ctx1);
        }
    }

    SWP(28, 25)
}

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input>\n", argv[0]);
        return 1;
    }

    if (strlen(argv[1]) != 32) {
        puts("Invalid");
        return 0;
    }

    memcpy((void *) inp, argv[1], 32);

    getcontext(&ctx1);
    ctx1.uc_stack.ss_sp = stack1;
    ctx1.uc_stack.ss_size = sizeof(stack1);
    ctx1.uc_link = &ctx2;
    makecontext(&ctx1, func1, 0);

    getcontext(&ctx2);
    ctx2.uc_stack.ss_sp = stack2;
    ctx2.uc_stack.ss_size = sizeof(stack2);
    ctx2.uc_link = &ctx_main;
    makecontext(&ctx2, func2, 0);

    swapcontext(&ctx_main, &ctx1);

    /*for (int i = 0; i < 32; i++) {
        printf("0x%hhx, ", inp[i]);
    }*/

    if (memcmp((void *) inp, expected, 32) == 0) {
        puts("Valid");
    } else {
        puts("Invalid");
    }
}
