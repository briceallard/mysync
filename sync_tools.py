import os
import time
import sys
import subprocess
from user import User


class sync_tool:

    def __init__(self):
        """
        :par
        """
        self.user = User()
        self.check_local_remote_mount_path()

    def mount_remote_server(self):
        """
        :param: none
        :description: Mounts the local server to the local machine.
        """
        mnt_cmd= "sshfs {0}{1}{2}{3}{4} {5}".format(self.user.get_user_name(),'@',self.user.get_server_ip(),":",self.user.get_remote_path(),
                                                 self.user.get_local_remote_mount())
        os.system(mnt_cmd)

    def check_local_remote_mount_path(self):
        """
        :params: none
        :description: checks that mount point exists on local machine, if not present, default directory is created @
                      ~/MySyncRemote/
        """
        MySyncRemote = os.path.expanduser(self.user.get_local_remote_mount())
        if(not os.path.isdir(MySyncRemote)):
            os.mkdir(MySyncRemote)

    def unmount_remote_directory(self):
        """
        :params: none
        :description: unmounts the local mount of the remote directory located @ ~/MySyncRemote, or the user 
                      defined location in config.json
        """
        unmount_command = "fusermount -u {0}".format(os.path.expanduser(self.user.get_local_remote_mount()))
        err = os.system(unmount_command)
        return True if(err == 0) else False

    def push_to_server(self, local_directory):
        """
        :params local_directory: copies file from local to remote mounted directory
        :description: copies a file to the remotely mounted local drive
        """
        local_directory = os.path.expanduser(local_directory)
        copy = "cp {0} {1}".format(local_directory,self.user.get_local_remote_mount())
        err = os.system(copy)
        return True if(err == 0) else False

    def pull_from_server(self, remote_directory, local_directory):
        """
        :params remote_directory: path file will be copied from
        :params local_directory: path file will be copied to
        :description: copies a file from the remote mounted dir to a local directory
        """
        local_directory = os.path.expanduser(local_directory)
        remote_directory = os.path.expanduser(remote_directory)
        copy = "cp {0} {1}".format(remote_directory, local_directory)
        err = os.system(copy)
        return True if (err == 0) else False

    def two_way_sync(self, local_directory, remote_directory):
        ...

    def delete_from_remote(self, path):
        """
        :params path: path to be deleted from remote mounted directory
        :description: deletes the file or folder located on the remotely mounted directory
        """
        delete_path = os.path.expanduser(path)
        cmd = "rm -rf {0}".format(delete_path) 
        err = os.system(cmd)
        return True if (err == 0) else False

    def add_directory_remote(self, new_dir_path):
        """
        :params new_dir_path: path of new directory to be created
        :description: a new directory will be created at the new_dir_path
        """
        new_dir_path = os.path.expanduser(new_dir_path)
        cmd = "mkdir {0}".format(new_dir_path)
        err = os.system(cmd)
        return True if (err == 0) else False

    



