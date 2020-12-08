import sys
sys.path.append("..")
from program import Program

def main():
    console = Program(boot_code="input.txt")
    console.run()


if __name__ == "__main__":
    main()