# project3.py
#
# ICS 33 Fall 2023
# Project 3: Why Not Smile?
#
# The main module that executes your Grin interpreter.
#
# WHAT YOU NEED TO DO: You'll need to implement the outermost shell of your
# program here, but consider how you can keep this part as simple as possible,
# offloading as much of the complexity as you can into additional modules in
# the 'grin' package, isolated in a way that allows you to unit test them.
import read
import grin


def main() -> None:
    """The main function that executes the Grin interpreter."""
    try:
        read.run_program()
    except grin.GrinParseError:
        print("Parsing error occurred...")
    except grin.GrinLexError:
        print("Lexing error occurred...")
    except ZeroDivisionError:
        print('Cannot divide integers or floats by 0.')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
