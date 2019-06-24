#!/usr/bin/python

"""
Author - Vishwanath Malipatil <vishmalipatil@gmail.com>
Date - 15/06/2019

This is git utility package which has necessary methods to use git commands from Python

"""

import os
import subprocess

class GitCommandMethods:
    def __init__(self):
        pass

    def executeShellCommand(self, cmd, working_directory):
        """
        Executes a shell command in a subprocess, waiting until it has completed.
        :param cmd: Command to execute.
        :param work_dir: Working directory path.
        """
        pipe = subprocess.Popen(cmd, shell=True, cwd=working_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (out, error) = pipe.communicate()
        print (out, error)
        pipe.wait()

    def gitAdd(self, file_path, repo_directory):
        """
        Adds the file at supplied path to the Git index.
        File will not be copied to the repository directory.
        No control is performed to ensure that the file is located in the repository directory.
        :param file_path: Path to file to add to Git index.
        :param repo_directory: Repository directory.
        """
        # print(" FilePath passed  %s " % file_path)
        # print(" Repo directory %s " % repo_directory)
        cmd = 'git add ' + str(file_path)
        self.executeShellCommand(cmd, repo_directory)

    def gitCommit(self, commit_message,repo_directory):
        """
        Commits the Git repository located in supplied repository directory with the supplied commit message.
        :param commit_message: Commit message.
        :param repo_dir: Directory containing Git repository to commit.
        """
        cmd = 'git commit -am "%s"' % commit_message
        self.executeShellCommand(cmd, repo_directory)
    
    def gitPush(self, repo_directory):
        """
        Pushes any changes in the Git repository located in supplied repository directory to remote git repository.
        :param repo_dir: Directory containing git repository to push.
        """
        cmd = 'git push '
        self.executeShellCommand(cmd, repo_directory)
    
    def gitGetCommits(self, parameter_list):
        pass
    
    def gitGetLastCommit(self, parameter_list):
        pass
    

if __name__ == "__main__":
    pass


