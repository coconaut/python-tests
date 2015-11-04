__author__ = 'coconaut'

import io


def read_file():
    with io.open("sample_text.txt", 'r') as stream:
        line = stream.readline()
        print "First line: \n%sa" % line
        print "The rest: \n"
        # can use for / else (weird...) to detect EOF
        for line in stream:
            print line
        else:
            print "Reached the end of the file"


def read_and_write():
    # open mode 'a' will append to file
    with io.open("brak.txt", 'r') as brak_file:
        with io.open("sample_text.txt", 'a') as sample_file:
            sample_file.write(unicode("\n\n"))
            for line in brak_file:
                sample_file.write(line)


if __name__ == '__main__':
    read_file()
    read_and_write()
    print "Done writing"
    read_file()



