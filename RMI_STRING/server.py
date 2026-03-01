#!/usr/bin/env python3
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class StringManipulator:
    """Class containing string manipulation functions"""
    
    # 1. Reverse a string
    def reverse_string(self, text):
        """Reverse the given string"""
        if text is None:
            return None
        return text[::-1]
    
    # 2. Convert to uppercase
    def to_uppercase(self, text):
        """Convert string to uppercase"""
        if text is None:
            return None
        return text.upper()
    
    # 3. Convert to lowercase
    def to_lowercase(self, text):
        """Convert string to lowercase"""
        if text is None:
            return None
        return text.lower()
    
    # 4. Count vowels in a string
    def count_vowels(self, text):
        """Count number of vowels in string"""
        if text is None:
            return 0
        vowels = "AEIOUaeiou"
        count = sum(1 for char in text if char in vowels)
        return count
    
    # 5. Check if string is palindrome
    def is_palindrome(self, text):
        """Check if string is a palindrome"""
        if text is None:
            return False
        # Remove spaces and convert to lowercase for comparison
        cleaned = text.replace(" ", "").lower()
        return cleaned == cleaned[::-1]
    
    # 6. Additional: Get string length
    def get_length(self, text):
        """Get length of string"""
        if text is None:
            return 0
        return len(text)
    
    # 7. Additional: Capitalize first letter
    def capitalize_first(self, text):
        """Capitalize first letter of each word"""
        if text is None:
            return None
        return text.title()

# Restrict to a particular path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def main():
    # Create server
    server = SimpleXMLRPCServer(("0.0.0.0", 5000),
                                requestHandler=RequestHandler,
                                allow_none=True)
    server.register_introspection_functions()
    
    # Create an instance of the manipulator
    manipulator = StringManipulator()
    
    # Register instance methods
    server.register_instance(manipulator)
    
    # Register functions individually (alternative)
    server.register_function(manipulator.reverse_string)
    server.register_function(manipulator.to_uppercase)
    server.register_function(manipulator.to_lowercase)
    server.register_function(manipulator.count_vowels)
    server.register_function(manipulator.is_palindrome)
    
    print("=" * 50)
    print("String Manipulator Server Starting...")
    print("=" * 50)
    print(f"Server address: http://0.0.0.0:5000")
    print("\nAvailable functions:")
    print("  - reverse_string(text)")
    print("  - to_uppercase(text)")
    print("  - to_lowercase(text)")
    print("  - count_vowels(text)")
    print("  - is_palindrome(text)")
    print("  - get_length(text)")
    print("  - capitalize_first(text)")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        # Run the server
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer shutting down...")
        print("Goodbye!")

if __name__ == "__main__":
    main()
