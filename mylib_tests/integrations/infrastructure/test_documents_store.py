# coding=utf-8
import os
import unittest

from mylib.infrastructure.documents_store import write_document_text, read_document_text
from mylib_tests.fixtures import clone_fixture


class DocumentsStoreTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_documents_store_convert_content_into_sha1_hash_as_document_reference(self):
        with clone_fixture('empty_document_store') as f:
            # Assign
            # Acts
            write_document_text(f, 'this the content')

            # Assert
            expected_file_path = '{0}/200489eead7a88a561184682b232b977ec760c57.txt'.format(f)
            self.assertTrue(os.path.isfile(expected_file_path))

    def test_documents_store_read_file_from_reference(self):
        with clone_fixture('document_store') as f:
            # Assign
            # Acts
            content = read_document_text(f, '200489eead7a88a561184682b232b977ec760c57')

            # Assert
            self.assertEqual(content, 'this the content')
