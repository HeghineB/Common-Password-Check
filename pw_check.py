import sys

def main(argv):

    # input validation
    if len(argv) == 1:
        print("ERROR: requires input argument")
    elif len(argv) > 2:
        print("ERROR: Too many arguments")
    else:
        target = argv[0]
        fp = open('word_bank')
        # returns a list of each line without EOL character
        lines = fp.read().splitlines()
        fp.close()

        for l in lines:
            if target == l:
                print("Common password")
                return
        print("Not common password")

if __name__ == '__main__':
    main(sys.argv)
