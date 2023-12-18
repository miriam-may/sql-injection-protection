# SQL Injection warning

Pretty simple, not world breaking. Runs any user input through the appropriate function to check for suspicious input. Prints message, creates alert and returns True if suspicious input is detected.

Options are 

1. Check for SQL keywords in input -> **find_suspicious_words()**
2. Check for non-numeric characters (for numeric only user input) -> **only_digits()**
3. Check for oversized user input (a username or password will not be as many characters as an SQL statement or short script). Default value is 20 characters -> **limited_length()**

I decided to show an example use-case by making it as a simple Flask app. 

I check for oversized input as well as numeric-only input in the ID field, as you don't want to let through malicious scripts that have been encoded.


