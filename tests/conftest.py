import os
import pathlib

import numpy as np
import pytest

import finalfusion
import finalfusion.vocab
import finalfusion.compat


@pytest.fixture
def tests_root():
    yield pathlib.PurePath(os.path.dirname(__file__))


@pytest.fixture
def simple_vocab_fifu(tests_root):
    yield finalfusion.vocab.load_vocab(tests_root / "data/simple_vocab.fifu")


@pytest.fixture
def vocab_array_tuple(tests_root):
    with open(tests_root / "data" / "embeddings.txt") as f:
        lines = f.readlines()
        v = []
        m = []
        for line in lines:
            line = line.split()
            v.append(line[0])
            m.append([float(p) for p in line[1:]])
    yield v, np.array(m, dtype=np.float32)


@pytest.fixture
def embeddings_fifu(tests_root):
    yield finalfusion.load_finalfusion(tests_root / "data" / "embeddings.fifu",
                                       mmap=False)


@pytest.fixture
def bucket_vocab_embeddings_fifu(tests_root):
    yield finalfusion.load_finalfusion(tests_root / "data" / "ff_buckets.fifu")


@pytest.fixture
def embeddings_text(tests_root):
    yield finalfusion.compat.load_text(
        os.path.join(tests_root, "data/embeddings.txt"))


@pytest.fixture
def embeddings_text_dims(tests_root):
    yield finalfusion.compat.load_text_dims(
        os.path.join(tests_root, "data/embeddings.dims.txt"))


@pytest.fixture
def embeddings_w2v(tests_root):
    yield finalfusion.compat.load_word2vec(
        os.path.join(tests_root, "data/embeddings.w2v"))


@pytest.fixture
def embeddings_ft(tests_root):
    yield finalfusion.compat.load_fasttext(
        os.path.join(tests_root, "data/fasttext.bin"))
