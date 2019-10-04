import os
import shutil
import tempfile

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
