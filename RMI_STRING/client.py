#!/usr/bin/env python3
import xmlrpc.client
import sys

class StringManipulatorClient:
    def __init__(self, host="0.0.0.0", port=5000):
        """Initialize client connection to server"""
        server_url = f"http://{host}:{port}"
        try:
            self.proxy = xmlrpc.client.ServerProxy(server_url, allow_none=True)
            print(f" Connected to server at {server_url}")
        except Exception as e:
            print(f" Failed to connect to server: {e}")
            sys.exit(1)
    
    def test_all_functions(self, text):
        """Test all string manipulation functions"""
        print("\n" + "=" * 60)
        print(f"TESTING ALL FUNCTIONS WITH: '{text}'")
        print("=" * 60)
        
        try:
            print(f" Original string    : {text}")
            print(f" Reversed           : {self.proxy.reverse_string(text)}")
            print(f" Uppercase           : {self.proxy.to_uppercase(text)}")
            print(f" Lowercase           : {self.proxy.to_lowercase(text)}")
            print(f" Vowel count        : {self.proxy.count_vowels(text)}")
            
            is_pal = self.proxy.is_palindrome(text)
            palindrome_status = " Yes" if is_pal else " No"
            print(f" Is palindrome?     : {palindrome_status}")
            
            # Additional functions
            print(f" Length             : {self.proxy.get_length(text)}")
            print(f" Capitalized        : {self.proxy.capitalize_first(text)}")
            
        except Exception as e:
            print(f" Error: {e}")
    
    def interactive_menu(self):
        """Display interactive menu for user"""
        while True:
            print("\n" + "=" * 60)
            print(" STRING MANIPULATOR - MAIN MENU")
            print("=" * 60)
            print("1.  Reverse a string")
            print("2.  Convert to uppercase")
            print("3.  Convert to lowercase")
            print("4.  Count vowels")
            print("5.  Check if palindrome")
            print("6.  Test all functions")
            print("7.  Get string length")
            print("8.  Capitalize words")
            print("9.  Run demo examples")
            print("0.  Exit")
            print("-" * 60)
            
            choice = input("Enter your choice (0-9): ").strip()
            
            if choice == "0":
                print("\n Goodbye!")
                break
            
            elif choice in ["1", "2", "3", "4", "5", "7", "8"]:
                text = input("Enter a string: ").strip()
                
                if not text:
                    print(" Please enter a valid string!")
                    continue
                
                try:
                    if choice == "1":
                        result = self.proxy.reverse_string(text)
                        print(f"\n Reversed string: '{result}'")
                    
                    elif choice == "2":
                        result = self.proxy.to_uppercase(text)
                        print(f"\n Uppercase: '{result}'")
                    
                    elif choice == "3":
                        result = self.proxy.to_lowercase(text)
                        print(f"\n Lowercase: '{result}'")
                    
                    elif choice == "4":
                        result = self.proxy.count_vowels(text)
                        print(f"\n Number of vowels: {result}")
                    
                    elif choice == "5":
                        result = self.proxy.is_palindrome(text)
                        if result:
                            print(f"\n '{text}' IS a palindrome!")
                        else:
                            print(f"\n '{text}' is NOT a palindrome!")
                    
                    elif choice == "7":
                        result = self.proxy.get_length(text)
                        print(f"\n String length: {result}")
                    
                    elif choice == "8":
                        result = self.proxy.capitalize_first(text)
                        print(f"\n Capitalized: '{result}'")
                        
                except Exception as e:
                    print(f"Error: {e}")
            
            elif choice == "6":
                text = input("Enter a string to test all functions: ").strip()
                if text:
                    self.test_all_functions(text)
                else:
                    print("Please enter a valid string!")
            
            elif choice == "9":
                self.run_demo_examples()
            
            else:
                print("Invalid choice! Please enter a number between 0-9.")
    
    def run_demo_examples(self):
        """Run some demo examples"""
        examples = [
            "hello world",
            "Python",
            "madam",
            "A man a plan a canal Panama",
            "racecar",
            "Hello 123"
        ]
        
        print("\n" + "=" * 60)
        print("RUNNING DEMO EXAMPLES")
        print("=" * 60)
        
        for example in examples:
            self.test_all_functions(example)
            input("\nPress Enter to continue...")

def main():
    print("PYTHON XML-RPC STRING MANIPULATOR")
    print("=" * 40)
    
    # Get server details from user (optional)
    use_default = input("Use default server (0.0.0.0:5000)? (y/n): ").strip().lower()
    
    if use_default == 'y' or use_default == '':
        host, port = "0.0.0.0", 5000
    else:
        host = input("Enter server host (default: 0.0.0.0): ").strip() or "0.0.0.0"
        port_input = input("Enter server port (default: 5000): ").strip()
        port = int(port_input) if port_input else 5000
    
    # Create client and start interactive menu
    try:
        client = StringManipulatorClient(host, port)
        client.interactive_menu()
    except KeyboardInterrupt:
        print("\n\n Goodbye!")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
