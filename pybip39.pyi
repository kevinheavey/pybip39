class Mnemonic:
    def __init__(self, word_count: int, language: str = "en") -> None: ...
    @staticmethod
    def from_entropy(entropy: bytes, language: str = "en") -> Mnemonic: ...
    @staticmethod
    def from_phrase(phrase: str, language: str = "en") -> Mnemonic: ...
    @staticmethod
    def validate(phrase: str, language: str = "en") -> None: ...
    @property
    def entropy(self) -> bytes: ...
    @property
    def phrase(self) -> str: ...
    def hex(self) -> str: ...
    def __str__(self) -> str: ...
    def __bytes__(self) -> bytes: ...
