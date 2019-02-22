import os
from subprocess import call as cmd

class GitClient(object):
    def __init__(self):
        self.sh = 'sh'
        self.package = os.path.dirname(__file__)
        self.author_renaming_script = package + '/author_renaming.sh'
        self.change_email_script = package + '/change_email.sh'
        self.rename_branch_script = package + '/rename_branch.sh'

    def author_renaming_command(self, old_name, new_name):
        return [self.sh, self.author_renaming_script, old_name, new_name]

    def change_email_command(self, old_email, new_email):
        return [self.sh, self.change_email_script, old_email, new_email]

    def rename_branch_command(self, old_name, new_name):
        return [self.sh, self.rename_branch_script, old_name, new_name]

    def change_email(self, old_email, new_email):
        cmd(self.change_email_command(old_email, new_email))

    def author_renaming(self, old_name, new_name):
        cmd(self.author_renaming_command(old_name, new_name))

    def rename_branch(self, old_name, new_name):
        cmd(self.rename_branch_command(old_name, new_name))

    def change_email_and_name(self, old_email, new_email, old_name, new_name):
        self.change_email(old_email, new_name)
        self.author_renaming(old_name, new_name)

        