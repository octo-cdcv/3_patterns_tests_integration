# coding=utf-8
import os
import unittest
import docker

from elasticsearch import Elasticsearch

from mylib.infrastructure.elasticsearch_search import ElasticsearchSearch
from mylib_tests import fixtures
from mylib_tests.fixtures import docker_fixture


class ElasticsearchSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        '''
        ce setup est chargée une seule fois au début de la suite
        de tests ElasticsearchSearchTest. L'instance d'elasticsearch
        reste up pendant tous les tests qui sont exécutés par cette classe.

        '''
        fixtures.check_port_is_available('localhost', 9200)
        cls.search = fixtures.docker_fixture_up('search')

    @classmethod
    def tearDownClass(cls) -> None:
        fixtures.docker_fixture_down(cls.search)

    def setUp(self) -> None:
        es = Elasticsearch(['localhost:9200'])
        self.elasticsearch = ElasticsearchSearch(es, 'search_000')
        self.docker_client = docker.from_env()
        docker_fixture.wait_docker_terminate(self.docker_client, 'elasticdump')

    def tearDown(self) -> None:
        self.docker_client.close()

    def test_search_should_return_a_match(self):
        # Assign
        query = 'git'

        # Acts
        result = self.elasticsearch.search('git')

        #Assert
        self.assertEqual('health_check.odt', result[0]['file_path'])
