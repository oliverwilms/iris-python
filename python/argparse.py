import argparse

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a function from the command line with arguments for name and age.")
    parser.add_argument("name", type=str, help="Your name, which will be used in the greeting message.")
    parser.add_argument("age", type=int, help="Your age, which will be included in the greeting message.")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose mode for additional output.")
    args = parser.parse_args()

    if args.verbose:
        print("Verbose mode enabled. Preparing to greet the user...")
    greet(args.name, args.age)
    if args.verbose:
        print("Greeting completed successfully.")
