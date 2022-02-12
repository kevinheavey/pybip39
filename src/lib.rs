use bip39::{Language, Mnemonic as MnemonicOriginal, MnemonicType, Seed};
use pyo3::{exceptions::PyValueError, prelude::*};

fn resolve_language(lang: &str) -> PyResult<Language> {
    let res = Language::from_language_code(lang)
        .ok_or_else(|| PyValueError::new_err(format!("Unrecognized language code: {}", lang)))?;
    Ok(res)
}

#[pyclass]
struct Mnemonic(MnemonicOriginal);

#[pymethods]
impl Mnemonic {
    #[new]
    pub fn new(word_count: usize, language: &str) -> PyResult<Self> {
        let mnemonic_type = MnemonicType::for_word_count(word_count)?;
        let resolved_language = resolve_language(language)?;
        Ok(Self(MnemonicOriginal::new(
            mnemonic_type,
            resolved_language,
        )))
    }
    #[staticmethod]
    pub fn from_entropy(entropy: &[u8], language: &str) -> PyResult<Self> {
        let lang = resolve_language(language)?;
        let underlying = MnemonicOriginal::from_entropy(entropy, lang)?;
        Ok(Self(underlying))
    }
    #[staticmethod]
    pub fn from_phrase(phrase: &str, language: &str) -> PyResult<Self> {
        let lang = resolve_language(language)?;
        let underlying = MnemonicOriginal::from_phrase(phrase, lang)?;
        Ok(Self(underlying))
    }

    #[staticmethod]
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
}

#[pymodule]
fn pybip39(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Mnemonic>()?;
    Ok(())
}
