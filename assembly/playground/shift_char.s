# CLI Argument
.equ ARG_NUM, 0
.equ ARG_0, 8
.equ ARG_1, 16
.equ ARG_2, 24

# Syscall code
.equ SYS_EXIT, 60
.equ SYS_WRITE, 1

# Standard file descriptors
.equ STDOUT, 1

# ASCII Characters boundary
.equ UPPERCASE_A, 65
.equ UPPERCASE_Z, 90
.equ LOWERCASE_A, 97
.equ LOWERCASE_Z, 122
.equ NULL_TERMINATE_ASCII, 0
.equ END_LINE_ASCII, 10
.equ ZERO_ASCII, 48

.section .text
.globl _start


# debugger
# movq %rdx, %rsi
# jmp exit
#
# There is still a bug that:
# when shifted with small number (1, 2, 10), it will be working such 'A' shift 1 becomes 'B'
# but it doesn't shift well with big (75)
# When I fixed for shifting with big shifter, it won't work with small number
# 'A' shift 1 causes infinte loop
# I belive this is due to how I do comparison between character and shifted value
# I'm also confused why do sometimes cmpb works for small shifter and cmpq work for big shifter
# Need to read understand more on how comparing by char and register works
_start:
    # Set bas pointer as stack pointer
    movq %rsp, %rbp
    movq ARG_1(%rbp), %rbx  # cli 'data' = *char[]
    movq $0, %rsi           # index of the character, starts with 0

    #movq ARG_2(%rbp), %rcx  # cli 'shifter' = *char[]
    #movq (%rcx), %rcx       # dereference 'shifter' to get its value (in ASCII decimal)
    #subq $ZERO_ASCII, %rcx  # substract rcx value with 48 to get it's number

    # HACK: inject %rcx with literal numbers for testing
    movq $56, %rcx

    # FUNCTION: Add shifter to original
    pushq %rcx      # argument #3: number to shift
    pushq %rsi      # argument #2: index of char
    pushq %rbx      # argument #1: *char[] to data
    call shift_character
    popq %rbx
    popq %rsi
    popq %rcx
    # ======= #

    # move *char[] in rbx into rsi
    movq (%rbx), %rsi

exit:
    movq %rsi, %rdi
    movq $SYS_EXIT, %rax
    syscall

shift_character:         # *[]char %rbx, index %rsi, shifter %rcx
    pushq %rbp
    movq %rsp, %rbp

    movq 16(%rbp), %rbx # First argument: *[]char
    movq 24(%rbp), %rsi # Second argument: index
    movq 32(%rbp), %rcx # Third argument: shifter

    # Fetch nth element into rdx
    # ASCII characters at most in 7 bits if I'm not mistaken
    movzbq (%rbx, %rsi, 1), %rdx

    is_uppercase_or_lowercase:
        cmpb $UPPERCASE_A, %dl
        jl not_upper_nor_lower   # if %dl < 65

        cmpb $UPPERCASE_Z, %dl  # if %dl <= 90
        jle is_upper

        cmpb $LOWERCASE_A, %dl  # if %dl < 97
        jl not_upper_nor_lower

        cmpb $LOWERCASE_Z, %dl  # if %dl < 122
        jle is_lower

        # Auto jump to not_upper_nor_lower if %dl > 122

    not_upper_nor_lower:
        jmp epilogue

    is_upper:
        addq %rcx, %rdx     # add shifter to nth element
        jmp check_wrap_upper

    is_lower:
        addq %rcx, %rdx
        jmp check_wrap_lower

    check_wrap_upper:
        cmpq $UPPERCASE_A, %rdx
        jl wrap_less_than_upper_a   # shifted char < 65

        cmpq $UPPERCASE_Z, %rdx
        jle epilogue                # shifted char within 65-90

        jmp wrap_more_than_upper_z  # shifted char > 90

    wrap_less_than_upper_a:
        # need to reconfirm
        addq $26, %rdx
        cmpq $UPPERCASE_A, %rdx
        jl wrap_less_than_upper_a   # loop again if shifted char still < 65
        jmp epilogue                # jmp to end if okay

    wrap_more_than_upper_z:
        # need to reconfirm
        subq $26, %rdx
        cmpq $UPPERCASE_Z, %rdx
        jg wrap_more_than_upper_z       # loop again if shited char > 90
        jmp epilogue                    # jmp to end if okay

    check_wrap_lower:
        cmpq $LOWERCASE_A, %rdx
        jl wrap_less_than_lower_a   # shifted char < 97

        cmpq $LOWERCASE_Z, %rdx
        jle epilogue                # shifted char within 97-122

        jmp wrap_more_than_lower_z  # shifted char > 122


    wrap_less_than_lower_a:
        # need to reconfirm
        addq $26, %rdx
        cmpq $LOWERCASE_A, %rdx
        jl wrap_less_than_lower_a   # loop again if shifted char still < 97
        jmp epilogue                # jmp to end if okay

    wrap_more_than_lower_z:
        # need to reconfirm
        subq $26, %rdx

        cmpq $LOWERCASE_Z, %rdx

        jg wrap_more_than_lower_z       # loop again if shited char > 122

        jmp epilogue # jmp to end if okay (%dl <= 122)

    epilogue:
        # store back nth element into *[]char
        movb %dl, (%rbx, %rsi, 1)
        movq %rbp, %rsp
        popq %rbp
        ret
