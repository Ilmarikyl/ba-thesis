import sys, os


def main(argv):

    if len(argv) != 2:
        print("Usage: python comparetogold.py <predictions_file> <gold_file>")
        sys.exit(2)

    linecount = 0

    infilename = argv[0].split("/")[-1]
    outfilename = "acc_"+infilename
    goldfilename = argv[1].split("/")[-1]
    
    infilepath = os.path.abspath(argv[0])
    outfilepath = infilepath.split("pred")[0] + outfilename
    goldfilepath = os.path.abspath(argv[1])

    try:
        with open(infilepath, 'r') as pred, open(goldfilepath, 'r') as gold, open(outfilepath, 'w') as outfile:
            wrong_n = 0
            
            for line1, line2 in zip(pred, gold):
                linecount += 1
                if line1 != line2:
                    wrong_n += 1

            percentage = ((linecount-wrong_n) / linecount) * 100
            print("{0:.2f}".format(percentage), file=outfile)

    except Exception as e:
        print(e)


if __name__ == "__main__":
   main(sys.argv[1:])

