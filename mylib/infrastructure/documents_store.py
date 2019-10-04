#!/usr/bin/python
# coding=utf-8
import io
import hashlib


def write_document_text(workdir, content: str):
    sha_1 = hashlib.sha1()
    sha_1.update(content.encode('utf-8'))
    doc_id = sha_1.hexdigest()

    with io.open('{0}/{1}.txt'.format(workdir, doc_id), 'w') as f:
        f.write(content)

    return doc_id


def read_document_text(workdir, doc_id: str):
    with io.open('{0}/{1}.txt'.format(workdir, doc_id), 'r') as f:
        file_content = f.read()

    return file_content
