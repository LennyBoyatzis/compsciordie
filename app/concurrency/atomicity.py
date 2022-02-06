"""
dis - Disassembler for CPython bytecode
"""
import dis

count = 0


def increment():
    global count
    count += 1


dis.dis(increment)
