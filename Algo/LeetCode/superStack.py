#!/bin/python3

import sys


# Complete the function below.

def handle_push(stack, operation):
    num = int(operation.split()[-1])
    stack.append([num, 0])
    print(num)

def handle_pop(stack, operation):
    x = stack.pop()
    if len(stack) != 0:
        stack[-1][1] += x[1]
        print(sum(stack[-1]))
    else:
        print("EMPTY")

def handle_inc(stack, operation):
    [ind, val] = [int(i) for i in operation.split()[1:]]
    stack[ind-1][1] += val
    if len(stack) != 0:
        print(sum(stack[-1]))
    else:
        print("EMPTY")    

def superStack(operations):
    stack = []
    for operation in operations:
        if operation.startswith("push"):
            handle_push(stack, operation)
        elif operation.startswith("pop"):
            handle_pop(stack, operation)
        elif operation.startswith("inc"):
            handle_inc(stack, operation)

if __name__ == "__main__":