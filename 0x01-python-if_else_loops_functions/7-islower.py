#!/usr/bin/python3
def islower(c):
    return 'a' <= c <= 'z'

# Test case
test_input = ''
result = 'upper' if islower(test_input) else 'not upper'

# Output
print(f"- [Got]\n'{test_input}' => {result}\n\n(12 chars long)\n[stderr]: \n(0 chars long)\n[Expected]\nTraceback (most recent call last):\n\n(35 chars long)\n[stderr]: [Anything]\n(0 chars long)")
