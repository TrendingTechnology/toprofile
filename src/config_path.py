import sys, os

if input("Configure color profile paths? (y/n) ") == "y":
    f = open(os.path.dirname(sys.argv[0]) + "/../paths.txt", "w")
    paths = []
    paths.append(input("Abs. path of viewing profile? "))
    paths.append(input("Abs. path of display profile? "))
    f.write(paths[0] + "\n")
    f.write(paths[1] + "\n")
    f.close()
    print("Configuration successfully saved")