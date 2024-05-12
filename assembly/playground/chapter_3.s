.equ    X, 1
.equ    Y, 1
.equ    Z, 2

.section .text
.globl _start

_start:
    movq $X, %rdi
    movq $Y, %rsi
    movq $Z, %rdx

scale3:
    leaq (%rsi, %rsi, 9), %rbx
    leaq (%rbx, %rdx), %rbx
    leaq (%rbx, %rdi, %rsi), %rbx

exit:
    movq %rbx, %rdi
    movq $60, %rax
    syscall
