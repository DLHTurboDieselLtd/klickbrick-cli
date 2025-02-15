# src/klickbrick_cli/__init__.py
import argparse
from src import hello  # Import the hello module

def main():
    parser = argparse.ArgumentParser(description="Klickbrick CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Create the parser for the "hello" command
    hello_parser = subparsers.add_parser("hello", help="Greets a person")
    hello_parser.add_argument("--name", help="The name of the person to greet")

    args = parser.parse_args()

    if args.command == "hello":
        hello.hello_command(args)  # Call the hello_command from hello.py
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
