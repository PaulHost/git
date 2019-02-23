#!/usr/bin/python

import sys
from src import GitClient

def main(argv):
    print(argv)
    if len(argv) == 1:
        print('Help:\n\
            change email on each commit: -e old_mail new_mail\n\
            change committer name on each commit: -n "old name" "new name"\n\
            change email and name: -e -n old_mail new_mail "old name" "new name"\n\
            rename branch: -r old_branch_name new_branch_name')
    else:
        client = GitClient()
        first_arg = argv.pop(0)
        if first_arg == '-e':
            second_arg = argv.pop(0)
            if second_arg == '-n':
                client.change_email_and_name(old_email=argv.pop(0),\
                                             new_email=argv.pop(0),\
                                             old_name=argv.pop(0),\
                                             new_name=argv.pop(0))
            else:
                client.change_email(second_arg, argv.pop(0))
        elif first_arg == '-n':
            client.author_renaming(old_name=argv.pop(0), new_name=argv.pop(0))
        elif  first_arg == '-r':
            client.rename_branch(old_name=argv.pop(0), new_name=argv.pop(0))



if __name__ == '__main__':
   main(sys.argv[1:])