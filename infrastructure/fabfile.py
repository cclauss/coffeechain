from fabric.api import *
from fabric.operations import *
from fabvenv import virtualenv
import time
import string
import random
import os.path


# Create random string
def random_generator(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


# Sawtooth ec2 node User
env.user = 'ubuntu'
# Sawtooth ec2 node keyfile
env.key_filename = '/home/bart/PycharmProjects/coffee-chain/Sawtooth-Korea.pem'
# Public ip's of nodes
all_hosts = [
    "ec2-13-124-172-115.ap-northeast-2.compute.amazonaws.com",
    "ec2-13-125-248-42.ap-northeast-2.compute.amazonaws.com",
    "ec2-13-125-150-84.ap-northeast-2.compute.amazonaws.com",
]

# Scantrust opt dir
scantrust_dir = '/opt/scantrust/'

# App name
app_name = 'coffeechain'
# Date of application version
app_random_value = random_generator()

# App root dir
app_root = scantrust_dir + 'sawtooth/' + app_name
# App version dir
app_version_dir = app_root + '/' + 'versions/' + app_random_value
# Virtual environment dir
home = app_version_dir + '/venv'

# Applicationfile to make process of
app_file = home + "/coffeechain/sawtooth/processor.py"

# Local path
local_path = '/home/bart/PycharmProjects/coffee-chain/'
# Path to zip-file to upload
app_zip = app_name + '.zip'
# Path to zip-file to upload
app_zip_path = local_path + app_zip

# Required python modules to be installed
modules = 'requirements.txt'
# Remote Path to requirements.txt
modules_path = home + "/coffeechain/server/" + modules

# Supervisor config file base
sup_file_base = '/etc/supervisor/conf.d/' + app_name
# Supervisor config file for this version
sup_file_version = sup_file_base + '_' + app_random_value + '.conf'
# Sym link
sym_link = "current_version"


@task
def allhosts():
    """
    Connect to all hosts
    allhosts [command]
    """
    env.hosts = all_hosts


@task
def doitall():
    """
    Do provisioning + application setup
    """
    provision()
    all_application()


@task
def provision():
    """
    Do provisioning only
    """
    update()
    installpython()
    create_app_directories()
    installsupervisor()
    installunzip()


@task
def update():
    """
    Update + upgrade system software
    """
    sudo("apt update")
    sudo("apt upgrade -y")


@task
def all_application():
    """
    Do application setup
    """
    create_version_directory()
    venv_stuff()
    upgradepip()
    upload_file(app_zip_path, app_zip)
    unzipfile(app_zip, app_file)
    installmodules()
    supervisor_stuff()
    activate_proc()


@task
def application():
    """
    Do application setup
    """
    create_version_directory()
    venv_stuff()
    upgradepip()
    upload_file(app_zip_path, app_zip)
    unzipfile(app_zip, app_file)
    installmodules()
    activate_proc()


@task
def activate_proc():
    reload()
    start(app_name)
    tail(app_name)
    status()


@task
def installpython():
    """
    Install python requirements
    """
    sudo("apt-get install -y python3-venv")
    sudo("apt-get install -y python-pip python-dev build-essential")


@task
def upgradepip():
    """
    upgrade pip + virtualenv
    """
    with virtualenv(home):
        sudo("pip install --upgrade pip")
        sudo("pip install --upgrade setuptools wheel virtualenv")


@task
def installsupervisor():
    """
    Install supervisor
    """
    sudo("apt-get install -y supervisor")


@task
def installunzip():
    """
    Install unzip
    """
    sudo("apt-get install -y unzip")


@task
def create_app_directories():
    """
    Create app root directory and assign permissions
    """
    # sudo("adduser --system --group scantrust")
    sudo("mkdir -p " + app_root + '/' + 'versions/')


@task
def create_version_directory():
    """
      Create version directory for application
    """
    sudo("mkdir -p " + app_version_dir)
    with cd(app_root):
        if os.path.isfile(sym_link):
            sudo("unlink " + sym_link)
        sudo("ln -s " + app_version_dir + " " + sym_link)


@task
def venv_stuff():
    """
    Setup virtual environement
    """
    sudo("python3 -m venv " + home)
    sudo("chown -R ubuntu:ubuntu " + app_root + '/' + 'versions/')
    run("source " + home + "/bin/activate")
    run("which python")


@task
def supervisor_stuff():
    """
    Create supervisor config file and start process
    """
    sudo(
        "echo '[program:" + app_name + "]\ndirectory=" + app_root + "/current_version/" + "\nhome=" + app_root + "/current_version/venv" +
        "\nprocess_name=%(program_name)s" + "\ncommand=" + app_root + "/current_version/venv/bin/python " + app_root + "/current_version/venv/coffeechain/sawtooth/processor.py"
        + "'>" + sup_file_base + '.conf')


@task
def upload_file(local_path, remote):
    """
    Uploads the application zip to the version directory of the app and unzip
    upload_app /full/local/path/file.zip file.zip
    """
    with cd(home):
        put(
            local_path=os.path.normpath(local_path),
            remote_path=remote,
            use_sudo=True
        )
        sudo("chown ubuntu:ubuntu %s" % remote)


@task
def unzipfile(zip, file):
    """
    Unzip a file
    """
    with cd(home):
        run("unzip " + zip)
        sudo("chown -R ubuntu:ubuntu " + file)
        sudo("rm " + zip)


@task
def installmodules():
    """
    Install all required modules for the application
    """

    with virtualenv(home):
        sudo("chown -R ubuntu:ubuntu " + app_root + '/' + 'versions/')
        run('which python')
        run('pip install -r ' + modules_path)


@task
def create_test_script():
    """
    Create test script to test virtual env
    """
    run("echo 'import arrow;"
        "\nwhile True:"
        "\n    print(arrow.utcnow())' > " + app_root + '/' + 'versions/' + app_file)


@task
def start(app_to_start):
    """
     start a supervisor process
     """
    sudo("supervisorctl start " + app_to_start)


@task
def restart(app_to_restart):
    """
    restart a supervisor process
    """
    sudo("supervisorctl restart " + app_to_restart)


@task
def stop(app_to_stop):
    """
    stop a supervisor process
    """
    sudo("supervisorctl stop " + app_to_stop)


@task
def tail(app_to_tail):
    """
    tail a supervisor process
    """
    sudo("supervisorctl tail " + app_to_tail)


@task
def reload():
    """
    reload supervisor (reload all processes)
    """
    sudo("supervisorctl reload")


@task
def status():
    """
    Get the status of all supervisor processes
    """
    sudo("supervisorctl status")
