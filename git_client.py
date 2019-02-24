#!/usr/bin/python

import sys
from src import GitClient


def main(argv):
    client = GitClient()
    first_arg = last(argv)
    if first_arg == 'help':
        print('Help:\n\
            change email on each commit: -e old_mail new_mail\n\
            change committer name on each commit: -n "old name" "new name"\n\
            change email and name: -e -n old_mail new_mail "old name" "new name"\n\
                -g renames or changed email global\n\
            rename branch: -r old_branch_name new_branch_name\n\
                       or  -r new_branch_name')
    elif first_arg == '-e':
        second_arg = last(argv)
        if second_arg == '-n':
            client.change_email_and_author(old_email=last(argv), \
                                           new_email=last(argv), \
                                           old_name=last(argv), \
                                           new_name=last(argv), \
                                           g=is_global(argv))
        else:
            client.change_email(second_arg, last(argv), g=is_global(argv))
    elif first_arg == '-n':
        client.author_renaming(old_name=last(argv), new_name=last(argv), g=is_global(argv))
    elif first_arg == '-r':
        client.rename_branch(name=last(argv), new_name=last(argv))

def last(argv):
    try:
        return argv.pop(0)
    except IndexError:
        return None


def is_global(argv):
    return last(argv) == '-g'


if __name__ == '__main__':
    main(sys.argv[1:])
