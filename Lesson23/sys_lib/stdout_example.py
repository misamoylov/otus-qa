import sys

while True:
    # output to stdout:
    print("Yet another iteration ...")
    try:
    # reading from sys.stdin (stop with Ctrl-D):
    number = input("Enter a number: ")
    except EOFError:
        print("\nciao")
        break
    else:
        number = int(number)
    if number == 0:
        print(sys.stderr, "0 has no inverse")
    else:
        print("inverse of %d is %f" % (number, 1.0/number))
# If we save the previous example under "streams.py" and use a file called "number.txt" with numbers (one number per line) for the input, we can call the script in the following way from the Bash shell:
# $ python streams.py < numbers.txt
# It's also possible to redirect the output into a file:
# $ python streams.py < numbers.txt > output.txt
# Now the only output left in the shell will be:
# 0 has no inverse
# because this comes via the sterr stream.