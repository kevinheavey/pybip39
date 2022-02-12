from pybip39 import MyEnum


def test_enum_equality() -> None:
    assert isinstance(MyEnum.Variant, MyEnum)


def compare_variants(variant1: MyEnum, variant2: MyEnum) -> bool:
    # reveal_type(variant1)
    # reveal_type(MyEnum.Variant)
    # reveal_type(MyEnum.OtherVariant)
    return variant1 == variant2


def test_comparison() -> None:
    assert not compare_variants(MyEnum.Variant, MyEnum.OtherVariant)


def test_int() -> None:
    assert int(MyEnum.Variant) == 0


def test_str() -> None:
    assert str(MyEnum.Variant) == "MyEnum.Variant"
