import sys

def main(argv):
    # input validation
    if len(argv) == 1:
        # No arguments passed in
        print("ERROR: requires input argument")
    elif len(argv) > 2:
        # More than one argument passed in
        print("ERROR: Too many arguments")
    else:
        # Valid Input
        target = argv[1]
        fp = open('word_bank')
        lines = fp.read().splitlines() # list containing each line; strips EOL character
        fp.close()
        # Check if input matches any words from work_bank
        for word in lines:
            if target == word:
                # match found
                print("Common password")
                return
        # No matches
        print("Not common password")

if __name__ == '__main__':
    main(sys.argv)
