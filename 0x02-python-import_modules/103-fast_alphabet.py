#!/usr/bin/python3
import sys; from string import ascii_uppercase as alphabet
sys.stdout.buffer.write(bytes(map(ord, alphabet))); sys.stdout.buffer.write(b'\n')
