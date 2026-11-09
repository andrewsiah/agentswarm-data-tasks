"""Standalone offline tag suggestions using vocabulary-provided example text."""

from collections import Counter
import math
import re
from typing import Mapping


_TOKEN_PATTERN = re.compile(r"[a-z0-9]+")


def _tokens(text: str) -> list[str]:
    return _TOKEN_PATTERN.findall(text.lower())


def suggest_tags(
    title: str,
    body: str,
    vocab: Mapping[str, list[str]],
    k: int = 3,
) -> list[str]:
    """Return up to ``k`` vocabulary tags ranked by text similarity."""
    if k == 0 or not vocab:
        return []

    query_counts = Counter(_tokens(title + " " + body))
    if not query_counts:
        return []

    tag_tokens = {tag: set(_tokens(tag)) for tag in vocab}
    documents = {
        tag: Counter(_tokens(tag + " " + " ".join(examples)))
        for tag, examples in vocab.items()
    }
    document_frequency = Counter(
        token
        for document in documents.values()
        for token in document
    )
    document_count = len(documents)

    def idf(token: str) -> float:
        return 1 + math.log(
            (1 + document_count) / (1 + document_frequency[token])
        )

    query_weights = {
        token: (1 + math.log(count)) * idf(token)
        for token, count in query_counts.items()
    }
    query_norm = math.sqrt(sum(weight * weight for weight in query_weights.values()))
    query_tokens = query_counts.keys()
    scored: list[tuple[float, str]] = []

    for tag, document in documents.items():
        document_weights = {
            token: (1 + math.log(count)) * idf(token)
            for token, count in document.items()
        }
        document_norm = math.sqrt(
            sum(weight * weight for weight in document_weights.values())
        )
        if query_norm and document_norm:
            dot_product = sum(
                weight * document_weights.get(token, 0)
                for token, weight in query_weights.items()
            )
            cosine = dot_product / (query_norm * document_norm)
        else:
            cosine = 0.0
        overlap = len(query_tokens & tag_tokens[tag])
        score = cosine + 2 * overlap
        if score > 0:
            scored.append((score, tag))

    scored.sort(key=lambda item: (-item[0], item[1]))
    return [tag for _, tag in scored[:k]]
