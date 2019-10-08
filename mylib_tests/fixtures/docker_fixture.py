import time

import docker


def wait_docker_terminate(client: docker.client, name: str) -> None:
    docker_terminate = False
    while not docker_terminate:
        try:
            docker_terminate = True if len(client.containers.list(filters={"label": "name={0}".format(name)})) == 0 else False
            time.sleep(1)
        except Exception as e:
            time.sleep(1)
