# src/klickbrick_cli/hello.py
import argparse


def hello_command(args):
    if args.name:
        name = args.name
    else:
        name = "World"
    print(f"Hello {name}")


def main():
    parser = argparse.ArgumentParser(description="Klickbrick hello command")
    parser.add_argument("--name", help="The name of the person to greet")
    args = parser.parse_args()
    hello_command(args)


if __name__ == "__main__":
    main()
