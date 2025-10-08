# Publishing to PyPI

## 1. Setup PyPI accounts
- Create account at https://pypi.org/account/register/
- Create account at https://test.pypi.org/account/register/ (for testing)
- Generate API tokens in account settings

## 2. Install build tools
```bash
pip install build twine
```

## 3. Build the package
```bash
python -m build
```

## 4. Test on TestPyPI first
```bash
twine upload --repository testpypi dist/*
```
Enter your TestPyPI API token when prompted.

Test install:
```bash
pip install --index-url https://test.pypi.org/simple/ nova-meta-prompter
```

## 5. Upload to PyPI
```bash
twine upload dist/*
```
Enter your PyPI API token when prompted.

## Tips:
- Add `dist/`, `build/`, `*.egg-info/` to `.gitignore`
- Store API tokens securely (can use `~/.pypirc` file)
- Increment version in `pyproject.toml` before each release
- Create git tags for releases: `git tag v0.1.0 && git push --tags`
