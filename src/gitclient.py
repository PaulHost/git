import os
from subprocess import call as cmd


class GitClient(object):
    def __init__(self):
        self.sh = 'sh'
        self.package = os.path.dirname(__file__) + '/sh_scripts'
        self.author_renaming_script = self.package + '/author_renaming.sh'
        self.change_email_script = self.package + '/change_email.sh'
        self.rename_branch_script = self.package + '/rename_branch.sh'
        self.rename_global_script = self.package + '/rename_global.sh'
        self.change_email_global_script = self.package + '/change_email_global.sh'

    def author_renaming_command(self, old_name, new_name):
        return [self.sh, self.author_renaming_script, old_name, new_name]

    def change_email_command(self, old_email, new_email):
        return [self.sh, self.change_email_script, old_email, new_email]

    def rename_branch_command(self, old_name, new_name):
        return [self.sh, self.rename_branch_script, old_name, new_name]

    def rename_global_command(self, new_global_name):
        return [self.sh, self.rename_branch_script, new_global_name]

    def change_email_global_command(self, new_global_email):
        return [self.sh, self.change_email_global_script, new_global_email]

    def change_email_global(self, new_global_email):
        cmd(self.change_email_global_command(new_global_email))

    def rename_global(self, new_global_name):
        cmd(self.rename_global_command(new_global_name))

    def change_email(self, old_email, new_email, g=False):
        cmd(self.change_email_command(old_email, new_email))
        if g:
            self.change_email_global(new_email)

    def author_renaming(self, old_name, new_name, g=False):
        cmd(self.author_renaming_command(old_name, new_name))
        if g:
            self.rename_global_command(new_name)

    def rename_and_change_email_global(self, new_email, new_name):
        self.change_email_global(new_email)
        self.rename_global(new_name)

    def change_email_and_author(self, old_email, new_email, old_name, new_name, g=False):
        self.change_email(old_email, new_email)
        self.author_renaming(old_name, new_name)
        if g:
            self.rename_and_change_email_global(new_email, new_name)

    def rename_branch(self, old_name, new_name):
        cmd(self.rename_branch_command(old_name, new_name))
