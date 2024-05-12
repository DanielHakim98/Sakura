# For CLI arguments
.equ ARG_NUM, 0
.equ ARG_0, 8
.equ ARG_1, 16

# Syscall code
.equ SYS_EXIT, 60
.equ SYS_WRITE, 1

# Standard file descriptors
.equ STDOUT, 1

# ASCII to decimal
.equ ZERO_ASCII, 48
.equ NINE_ASCII, 57


# string for displaying error
ERR_NOT_NUM:
    .string "Shifter is not a number\n"
END_ERR_NOT_NUM:
    LEN_ERR_NOT_NUM = . - ERR_NOT_NUM

.section .text
.globl _start

_start:
    # Set base pointer as stack pointer
    movq %rsp, %rbp

    # Extract argument 'shifter' from cli
    # it's a pointer to *char []
    movq ARG_1(%rbp), %rbx

    # CALL atoi: Get decimal value from argument
    pushq %rbx
    call atoi
    popq %rbx
    # move return value from atoi function
    movq %rax, %rsi

exit:
    movq %rsi, %rdi
    movq $SYS_EXIT, %rax
    syscall

atoi:
    prologue:
        pushq %rbp
        movq %rsp, %rbp
        movq 16(%rbp), %rbx

    head:
        # Dereference pointer in rbx and move the value to rsi
        movq $0, %rsi
        movq (%rbx, %rsi, 1), %rcx

        # Check if current value in rsi is a number
        cmpb $ZERO_ASCII, %cl      # Compare the value if 0 ASCII
        jl not_number              # If it's less than 0, jump to not_a_number
        cmpb $NINE_ASCII, %cl      # Compare the value with 9 ASCII
        jg not_number              # If it's greater than 57, jump to not_a_number

        # Substract with ASCII decimal 49 to get decimal number
        subq $ZERO_ASCII, %rcx
        movq $0, %rax
        addq %rcx,%rax

    next:
        # Increase current index by 1
        incq %rsi

        # Dereference pointer in rbx at current index and move into rsi
        movq (%rbx, %rsi, 1), %rcx

        # Check if current value is null terminated
        cmpb $0, %cl
        je epilogue

        # Check if current value in rsi is a number
        cmpb $ZERO_ASCII, %cl      # Compare the value if 0 ASCII
        jl not_number              # If it's less than 0, jump to not_a_number
        cmpb $NINE_ASCII, %cl      # Compare the value with 9 ASCII
        jg not_number              # If it's greater than 57, jump to not_a_number

        # Substract with ASCII decimal 49 to get decimal number
        subq $ZERO_ASCII, %rcx
        imulq $10, %rax
        addq %rcx, %rax

        jmp next

    epilogue:
        movq %rbp, %rsp
        popq %rbp
        ret

not_number:
    # Write *[]char to stdout
    movq $SYS_WRITE, %rax
    movq $STDOUT, %rdi
    movq $ERR_NOT_NUM, %rsi
    movq $LEN_ERR_NOT_NUM, %rdx
    syscall

    # Exit status
    movq $1, %rsi
    jmp exit




