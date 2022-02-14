use bip39::{Language, Mnemonic as MnemonicOriginal, MnemonicType, Seed as SeedOriginal};
use pyo3::{exceptions::PyValueError, prelude::*};

fn resolve_language(lang: &str) -> PyResult<Language> {
    let res = Language::from_language_code(lang)
        .ok_or_else(|| PyValueError::new_err(format!("Unrecognized language code: {}", lang)))?;
    Ok(res)
}

/// The primary type in this library, most tasks require creating or using one.
///
/// To create a *new* [`Mnemonic`][Mnemonic] from a randomly generated key, call [`Mnemonic::new()`][Mnemonic::new()].
///
/// To get a [`Mnemonic`][Mnemonic] instance for an existing mnemonic phrase, including
/// those generated by other software or hardware wallets, use [`Mnemonic::from_phrase()`][Mnemonic::from_phrase()].
///
/// You can get the HD wallet [`Seed`][Seed] from a [`Mnemonic`][Mnemonic] by calling [`Seed::new()`][Seed::new()].
/// From there you can either get the raw byte value with [`Seed::as_bytes()`][Seed::as_bytes()], or the hex
/// representation using Rust formatting: `format!("{:X}", seed)`.
///
/// You can also get the original entropy value back from a [`Mnemonic`][Mnemonic] with [`Mnemonic::entropy()`][Mnemonic::entropy()],
/// but beware that the entropy value is **not the same thing** as an HD wallet seed, and should
/// *never* be used that way.
#[pyclass]
struct Mnemonic(pub MnemonicOriginal);

#[pymethods]
impl Mnemonic {
    #[new]
    #[args(word_count = "12", language = "\"en\"")]
    pub fn new(word_count: usize, language: &str) -> PyResult<Self> {
        let mnemonic_type = MnemonicType::for_word_count(word_count)?;
        let resolved_language = resolve_language(language)?;
        Ok(Self(MnemonicOriginal::new(
            mnemonic_type,
            resolved_language,
        )))
    }
    #[staticmethod]
    #[args(language = "\"en\"")]
    pub fn from_entropy(entropy: &[u8], language: &str) -> PyResult<Self> {
        let lang = resolve_language(language)?;
        let underlying = MnemonicOriginal::from_entropy(entropy, lang)?;
        Ok(Self(underlying))
    }
    #[staticmethod]
    #[args(language = "\"en\"")]
    pub fn from_phrase(phrase: &str, language: &str) -> PyResult<Self> {
        let lang = resolve_language(language)?;
        let underlying = MnemonicOriginal::from_phrase(phrase, lang)?;
        Ok(Self(underlying))
    }

    #[staticmethod]
    #[args(language = "\"en\"")]
    pub fn validate(phrase: &str, language: &str) -> PyResult<()> {
        let lang = resolve_language(language)?;
        Ok(MnemonicOriginal::validate(phrase, lang)?)
    }

    #[getter]
    pub fn entropy(&self) -> &[u8] {
        self.0.entropy()
    }

    #[getter]
    pub fn phrase(&self) -> &str {
        self.0.phrase()
    }

    pub fn hex(&self) -> String {
        format!("{:x}", self.0)
    }

    pub fn __str__(&self) -> &str {
        self.phrase()
    }

    pub fn __bytes__(&self) -> &[u8] {
        self.entropy()
    }
}

#[pyclass]
struct Seed(pub SeedOriginal);

#[pymethods]
impl Seed {
    #[new]
    pub fn new(mnemonic: &Mnemonic, password: &str) -> Self {
        Self(SeedOriginal::new(&mnemonic.0, password))
    }

    pub fn __bytes__(&self) -> &[u8] {
        self.0.as_bytes()
    }

    pub fn hex(&self) -> String {
        format!("{:x}", self.0)
    }
}

#[pymodule]
fn pybip39(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Mnemonic>()?;
    m.add_class::<Seed>()?;
    Ok(())
}
