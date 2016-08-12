## Mengqi Li 92059150
## ICS 32

import os
import shutil

## required functions
def search_by_name() -> list:
    ''' Search files/folders that have exact name as user types '''
    key = input("Enter a file name (ex)filename.doc: ")
    result = []    
    result.extend(search_by_name2(os.getcwd(), key))
    return result

def search_by_name2(direct: str, key: str) -> list:
    ''' Recursive function for search_by_name '''
    result = []
    for content in os.listdir(direct):
        try:
            result.extend(search_by_name2(direct+'/'+content, key))
        except:
            pass
        if key.upper() == content.upper():
            result.append(os.path.abspath(direct+'/'+content))
    return result


def search_by_name_ending() -> list:
    ''' Search files/folders that have exact name ending as user types '''
    key = input("Enter a file ending (ex).pdf: ")
    result = []    
    result.extend(search_by_name_ending2(os.getcwd(), key))
    return result

def search_by_name_ending2(direct: str, key: str) -> list:
    ''' Recursive function for search_by_name_ending '''
    result = []
    for content in os.listdir(direct):
        try:
            result.extend(search_by_name_ending2(direct+'/'+content, key))
        except:
            pass
        if content.endswith(key):
            result.append(os.path.abspath(direct+'/'+content))
    return result


def search_by_size() -> list:
    ''' Search files/folders that have more size than user specifies '''
    key = int(input("Enter a file size (ex)1028: "))
    result = []    
    result.extend(search_by_size2(os.getcwd(), key))
    return result

def search_by_size2(direct: str, key: int) -> list:
    ''' Recursive function for search_by_size '''
    result = []
    for content in os.listdir(direct):
        try:
            result.extend(search_by_size2(direct+'/'+content, key))
        except:
            pass
        if os.stat(direct+'/'+content).st_size >= key:
            result.append(os.path.abspath(direct+'/'+content))
    return result

def print_path_only(files: list):
    ''' Print the file's path to the console '''
    for file in files:
        print('   ',os.path.abspath(file))
    return

def print_first_line_of_text(files: list):
    ''' Print the first line of text from file(s) to the console '''
    for file in files:
        print("\nFile name:",file)
        try:
            f = open(file, 'r')
            print('\t', f.readline())
            f.close()
        except:
            print("\tSorry, couldn't read", file)
    return

def copy_file(files: list):
    ''' Creates dupulicate file(s) from interested file(s) with extension ".dup" '''
    for file in files:
        try:
            shutil.copyfile(file, file+'.dup')
        except:
            print("Sorry, couldn't copy", file)
        else:
            print("Copy created: "+ str(file) +'.dup')
    return

def touch_file(files: list):
    ''' Modify file(s) last modified timestamp to be the current date/time '''
    for file in files:
        try:
            os.utime(file, None)
        except:
            open(file, 'a').close()
        finally:
            print(str(file), "touched")
    return

## support functions
def print_current_directory():
    ''' Prints out current directory '''
    print('\n\n\n------------------------------------------------')
    print('Current directory:\n   >>>',os.getcwd())
    print_directory()
    return

def print_directory():
    ''' Prints out file(s)/folder(s) that are in current directory '''
    for content in os.listdir(os.getcwd()):
        print('\t>>>', content)
    print()
    return

def print_interested_file(files: list):
    ''' Prints out interested file(s)/folder(s) that are selected by search '''
    print('\n\n\n------------------------------------------------')
    print("Interested file(s): ")
    for file in files:
        print('   ',file)
    return

Commands = {'SN':search_by_name,
            'SE':search_by_name_ending,
            'SS':search_by_size }
Actioncmd = {'PP':print_path_only,
             'PF':print_first_line_of_text,
             'CF':copy_file,
             'TF':touch_file}

def menu():
    ''' Prints out menu '''
    print_current_directory()
    print(' ----------------- Menu ------------------')
    print(' |NO.     Options                commands|')
    print(' |1.  Search by file name         cmd(SN)|')
    print(' |2.  Search by file name ending  cmd(SE)|')
    print(' |3.  Search by file size         cmd(SS)|')
    print(' |4.  Quit program                cmd(!Q)|')
    print(' |                                       |')
    print(' |    Or simply type directory to look up|')
    print(' -----------------------------------------')

def file_actions():
    ''' Prints out file actions user can take '''
    print(' ---------------- Actions ----------------')
    print(' |NO.     Options                commands|')
    print(' |1.  Print path only             cmd(PP)|')
    print(' |2.  Print first line of text    cmd(PF)|')
    print(' |3.  Copy file                   cmd(CF)|')
    print(' |4.  Touch file                  cmd(TF)|')
    print(' |5.  Go back                     cmd(GB)|')
    print(' -----------------------------------------')
    

## main function
while(True):
    try:
        menu()
        cmd = input("Command: ").upper()
        if cmd in Commands:
            interested = Commands[cmd]()
            if len(interested) != 0:
                while(True):
                    print_interested_file(interested)
                    file_actions()
                    action = input("Command: ").upper()
                    if action in Actioncmd:
                        Actioncmd[action](interested)
                    elif action == 'GB':
                        break
                    else:
                        print("wrong input")
            else:
                print("No file selected")
        elif cmd == '!Q':
            break
        else:
            if os.path.exists(cmd):
                os.chdir(cmd)
            else:
                print("Sorry, can't find directory / command")
    except:
        print("Sorry, something went wrong...")

print("program ended")































