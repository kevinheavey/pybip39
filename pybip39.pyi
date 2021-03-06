class Language:
    English: Language
    ChineseSimplified: Language
    ChineseTraditional: Language
    French: Language
    Italian: Language
    Japanese: Language
    Korean: Language
    Spanish: Language
    def __int__(self) -> int: ...

class MnemonicType:
    Words12: MnemonicType
    Words15: MnemonicType
    Words18: MnemonicType
    Words21: MnemonicType
    Words24: MnemonicType
    def __int__(self) -> int: ...

class Mnemonic:
    def __init__(
        self,
        mtype: MnemonicType = MnemonicType.Words12,
        language: Language = Language.English,
    ) -> None: ...
    @staticmethod
    def from_entropy(
        entropy: bytes, language: Language = Language.English
    ) -> Mnemonic: ...
    @staticmethod
    def from_phrase(phrase: str, language: Language = Language.English) -> Mnemonic: ...
    @staticmethod
    def validate(phrase: str, language: Language = Language.English) -> None: ...
    @property
    def entropy(self) -> bytes: ...
    @property
    def phrase(self) -> str: ...
    def hex(self) -> str: ...
    def __str__(self) -> str: ...
    def __bytes__(self) -> bytes: ...

class Seed:
    def __init__(self, mnemonic: Mnemonic, password: str) -> None: ...
    def __bytes__(self) -> bytes: ...
    def hex(self) -> str: ...
