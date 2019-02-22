#!/usr/bin/python

import os
import sys
from subprocess import call as cmd
from src import GitClient

def main(argv):
    if len(argv) == 1:
        print('Help:\n\
            change email on each commit: -e old_mail new_mail\n\
            change commiter name on each commit: -n "old name" "new name"\n\
            change email and name: -e -n old_mail new_mail "old name" "new name"\n\
            rename branch: -r old_branch_name new_branch_name')
    else:
        client = GitClient()
        first_arg = argv.pop
        if first_arg == '-e':
            second_arg = argv.pop
            if second_arg == '-n':
                client.change_email_and_name(argv.pop, argv.pop, argv.pop, argv.pop)
            else:
                client.change_email(argv.pop, argv.pop)
        elif first_arg == '-n':
            client.author_renaming(argv.pop, argv.pop)
        elif  first_arg == '-r':
            client.change_branch_name(argv.pop, argv.pop)


def change_email_command(argv):

if __name__ == '__main__':
   main(sys.argv[1:])