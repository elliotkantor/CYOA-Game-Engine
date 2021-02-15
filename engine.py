#! python3
import time
import sys
path = 'script.txt'
# ___ DOCS ____
# viewBeginning() takes no arguments and shows whatever comes before the first chunk
# openChunk() takes a string 'chunk [something]' as an argument and only executes what's within the chunk


def getChoice(options):
    # make user choose
    choice = '-2'
    # print(options)
    while (choice not in str(list(range(1, len(options)+1)))) and (choice not in options):
        choice = input('>> ').strip().lower()
        if choice in str(list(range(1, len(options) + 1))):
            choice = int(choice) - 1
            choice = options[choice].lower()
    # returns string name, not number
    return choice


def sp(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)
    print()


def viewBeginning():
    script = open(path, 'r')
    for line in script:
        line = line.strip()
        if line[:5] == 'chunk':
            break
        elif line == '':
            continue
        sp(line)
        # continue
    script.close()


def openChunk(startLine):
    temp = True
    used = False
    script = open(path, 'r')
    for line in script:
        line = line.strip()
        # only continues after reaches startline
        if line != startLine and temp:
            continue
        # removes empty lines
        if line == '':
            continue
        elif line[:5] == 'chunk' and not used:
            temp = False
            used = True
        elif line[:5] == 'chunk' and used:
            break
        elif line.lower() == 'pause':
            # prompts to enter to continue
            input("Press enter to continue. ")
        elif line.lower() == 'blank':
            print()
        elif line[:4].lower() == 'wait':
            try:
                amount = int(line[4:])
            except:
                amount = 1
            time.sleep(amount)
        elif line[0:6].lower() == 'choose':
            # get options as list
            global options
            options = line[6:].split(',')

            # print options
            print("Choose from the following: ")
            for i in range(len(options)):
                options[i] = options[i].strip()
                print(f'({i+1}) {options[i]}')
                options[i] = options[i].lower()
            # return options
        elif line[0] == '#':
            continue
        else:
            # if all else fails, print the line normally as text
            sp(line)

    script.close()

# order the script below


viewBeginning()
openChunk('chunk 1')
choice = getChoice(options)
if choice == 'bedroom':
    openChunk('chunk bedroom')
elif choice == 'bathroom':
    openChunk('chunk bathroom')
else:
    openChunk('chunk attic')
