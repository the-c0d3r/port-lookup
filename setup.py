import os


def install():
    file_path = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "port.py"
    install_path = "/usr/local/bin/portinfo"
    cmd = "sudo ln -s {} {}".format(file_path, install_path)
    cmd2 = "sudo chmod 775 {}".format(install_path)
    execute(cmd)
    execute(cmd2)

def uninstall():
    install_path = "/usr/local/bin/portinfo"
    cmd = "sudo rm {}".format(install_path)
    execute(cmd)

def execute(command):
    print("Executing : {}".format(command))
    os.system(command)


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("This file is used to install the program to system-wide")
        print("sudo python setup.py install")
        print("sudo python setup.py uninstall")
    else:
        if sys.argv[1] == "install":
            print("Installing port-lookup symlink to /usr/local/bin/portinfo")
            install()
            print("Installation completed!\ntype 'portinfo' to execute")
        elif sys.argv[1] == "uninstall":
            print("Uninstalling port-lookup symlink from /usr/local/bin/portinfo")
            uninstall()
            print("Uninstallation completed")
