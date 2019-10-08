import os
import shutil
import socket
import subprocess
import tempfile
from contextlib import closing

from decorator import contextmanager

SCRIPT_DIRECTORY_PATH = os.path.dirname(os.path.realpath(__file__))


@contextmanager
def clone_fixture(fixture_name, working_directory=None, remove_when_fails=True):
    try:
        working_directory = clone_fixture_up(fixture_name, working_directory)
        yield working_directory
    finally:
        clone_fixture_down(working_directory, remove_when_fails)


def clone_fixture_down(working_directory=None, remove_when_fails=True):
    if os.path.isdir(working_directory) and remove_when_fails:
        shutil.rmtree(working_directory)


def clone_fixture_up(fixture_name, working_directory=None):
    tmp_prefix = '{0}_{1}'.format(fixture_name, '_')
    working_directory = tempfile.mktemp(prefix=tmp_prefix) if not working_directory else working_directory
    template_working_directory = os.path.join(SCRIPT_DIRECTORY_PATH, fixture_name)
    if not os.path.isdir(template_working_directory):
        fixtures_list = [d for d in os.listdir(SCRIPT_DIRECTORY_PATH) if
                         os.path.isdir(os.path.join(SCRIPT_DIRECTORY_PATH, d))]
        raise Exception('the fixture {0} does not exists in fixtures : {1}'.format(fixture_name, fixtures_list))
    shutil.copytree(template_working_directory, working_directory)
    return working_directory


def docker_fixture_up(fixture_name, working_directory=None):
    dir = clone_fixture_up(fixture_name, working_directory)
    try:
        subprocess.check_output(
            ['docker-compose', '--file', os.path.join(dir, 'docker-compose.yml'), 'up', '--detach',
             '--force-recreate'],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as exception:
        raise OSError(exception.stdout)

    return dir


def docker_fixture_down(working_directory=None):
    subprocess.check_output(
        ['docker-compose', '--file', os.path.join(working_directory, 'docker-compose.yml'), 'down'],
        stderr=subprocess.STDOUT
    )
    clone_fixture_down(working_directory)


def check_port_is_available(host: str, port: int):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            raise OSError('port is already used on {0}/{1}'.format(host, port))
