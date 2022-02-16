from pybip39 import Mnemonic, Seed, Language

ENTROPY = bytes(
    [
        0x33,
        0xE4,
        0x6B,
        0xB1,
        0x3A,
        0x74,
        0x6E,
        0xA4,
        0x1C,
        0xDD,
        0xE4,
        0x5C,
        0x90,
        0x84,
        0x6A,
        0x79,
    ]
)


def seed_hex_format() -> None:
    mnemonic = Mnemonic.from_entropy(ENTROPY)
    seed = Seed(mnemonic, "password")

    assert (
        seed.hex()
        == "0bde96f14c35a66235478e0c16c152fcaf6301e4d9a81d3febc50879fe7e5438e6a8dd3e39bdf3ab7b12d6b44218710e17d7a2844ee9633fab0e03d9a6c8569b"
    )


def check_unicode_normalization(
    lang: Language, phrase: str, password: str, expected_seed_hex: str
) -> None:
    mnemonic = Mnemonic.from_phrase(phrase, lang)
    seed = Seed(mnemonic, password)
    assert seed.hex() == expected_seed_hex


# Test vector is derived from https://github.com/infincia/bip39-rs/issues/26#issuecomment-586476647
def issue_26() -> None:
    check_unicode_normalization(
        Language.Spanish,
        "camello pomelo toque oponer urgente lástima merengue cutis tirón pudor pomo barco",
        "el español se habla en muchos países",
        "67a2cf87b9d110dd5210275fd4d7a107a0a0dd9446e02f3822f177365786ae440b8873693c88f732834af90785753d989a367f7094230901b204c567718ce6be",
    )


def test_password_is_unicode_normalized() -> None:
    check_unicode_normalization(
        Language.English,
        "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about",
        "nullius　à　nym.zone ¹teſts² English",
        "61f3aa13adcf5f4b8661fc062501d67eca3a53fc0ed129076ad7a22983b6b5ed0e84e47b24cff23b7fca57e127f62f28c1584ed487872d4bfbc773257bdbc434",
    )


def test_japanese_normalization_1() -> None:
    check_unicode_normalization(
        Language.Japanese,
        "あいこくしん　あいこくしん　あいこくしん　あいこくしん　あいこくしん　あいこくしん　あいこくしん　あいこくしん　あいこくしん　あいこくしん　あいこくしん　あおぞら",
        "㍍ガバヴァぱばぐゞちぢ十人十色",
        "a262d6fb6122ecf45be09c50492b31f92e9beb7d9a845987a02cefda57a15f9c467a17872029a9e92299b5cbdf306e3a0ee620245cbd508959b6cb7ca637bd55",
    )


def test_japanese_normalization_2() -> None:
    check_unicode_normalization(
        Language.Japanese,
        "うちゅう　ふそく　ひしょ　がちょう　うけもつ　めいそう　みかん　そざい　いばる　うけとる　さんま　さこつ　おうさま　ぱんつ　しひょう　めした　たはつ　いちぶ　つうじょう　てさぎょう　きつね　みすえる　いりぐち　かめれおん",
        "㍍ガバヴァぱばぐゞちぢ十人十色",
        "346b7321d8c04f6f37b49fdf062a2fddc8e1bf8f1d33171b65074531ec546d1d3469974beccb1a09263440fc92e1042580a557fdce314e27ee4eabb25fa5e5fe",
    )


def test_french_normalization() -> None:
    check_unicode_normalization(
        Language.French,
        "paternel xénon curatif séparer docile capable exigence boulon styliste plexus surface embryon crayon gorge exister",
        "nullius　à　nym.zone ¹teſts² Français",
        "cff9ffd2b23549e73601db4129a334c81b28a40f0ee819b5d6a54c409999f0dfb6b89df17cae6408c96786165c205403d283baadc03ffdd391a490923b7d9493",
    )


def test_bytes() -> None:
    mnemonic = Mnemonic.from_entropy(ENTROPY)
    seed = Seed(mnemonic, "password")
    assert bytes(seed).hex() == seed.hex()
