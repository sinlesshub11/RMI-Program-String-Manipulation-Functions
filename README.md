**RMI Program – String Manipulation Functions**

This project demonstrates a simple Remote Method Invocation (RMI)-style application in Python. It allows clients to perform common string manipulation operations remotely, showcasing how distributed applications can be built where methods are executed on a server but invoked seamlessly from the client side.

**Available Functions:**

The program currently supports the following string operations:
- reverse_string – Reverses the characters in a string.
- to_uppercase – Converts all characters to uppercase.
- to_lowercase – Converts all characters to lowercase.
- count_vowels – Counts the number of vowels in the string.
- is_palindrome – Checks if the string reads the same forwards and backwards.
- get_length – Returns the total number of characters in the string.
- capitalize_first – Capitalizes the first character of the string.

**How It Works**
- The server hosts these string manipulation methods and exposes them via RMI-style remote calls.
- The client connects to the server and invokes these methods remotely.
- Communication between client and server is handled through Python’s remote object framework, making remote calls appear like local ones.
