import re

regex = r"^[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]$"

def test_string(string):
    if re.match(regex, string):
        print(f"'{string}' matches the regex.")
    else:
        print(f"'{string}' does not match the regex.")

# Test cases
test_string("a1")
test_string("abc123XYZ")
test_string("a-b-c-1-2-3")
test_string("long-alphanumeric-string-with-dashes123")
test_string("12")
test_string("A2")
test_string("a")
test_string("-abc")
test_string("abc-")
test_string("abc!")
test_string("very-long-string-that-exceeds-the-maximum-allowed-length123456789012345678901234567890123456789012345678901234567890")

# This Python code defines a function test_string that takes a string as input and uses re.match to check if the string matches the regex. The re.match function only matches at the beginning of the string, which is perfect for our needs given the ^ anchor in the regex. I added a bunch of test examples to test for success and failure.
# You are an expert regex string creator and understand how regex works. Your job is to convert the user's natural language queries and constraints in the form of regex. After generating the regex string, provide explanation in detail with a few examples. Then demonstrate its use in a python code.

# User query:
# Give me the regex equivalent of the following:
#My requirements are:

#I want my string to have 2-63 characters.

#The string should be alphanumeric and can contain - also.

#The string must start as well as end with alphanumeric characters only.*/
