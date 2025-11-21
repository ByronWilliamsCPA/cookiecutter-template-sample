# My Python Project

## Quality & Security

[![codecov](https://codecov.io/gh/ByronWilliamsCPA/cookiecutter-template-sample/graph/badge.svg)](https://codecov.io/gh/ByronWilliamsCPA/cookiecutter-template-sample)

## CI/CD Status

[![CI Pipeline](https://github.com/ByronWilliamsCPA/cookiecutter-template-sample/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/ByronWilliamsCPA/cookiecutter-template-sample/actions/workflows/ci.yml?query=branch%3Amaster)
[![Security Analysis](https://github.com/ByronWilliamsCPA/cookiecutter-template-sample/actions/workflows/security-analysis.yml/badge.svg?branch=master)](https://github.com/ByronWilliamsCPA/cookiecutter-template-sample/actions/workflows/security-analysis.yml?query=branch%3Amaster)

## Project Info

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://github.com/ByronWilliamsCPA/.github/blob/main/CODE_OF_CONDUCT.md)

---

## Overview

A short description of the project

This project provides:
- Core functionality for a short description of the project
- Production-ready code with comprehensive testing
- Well-documented API and architecture
- Security-first development practices

## Features

- **High Quality**: 60%+ test coverage enforced via CI
- **Type Safe**: Full type hints with MyPy strict mode
- **Well Documented**: Clear docstrings and comprehensive guides
- **Developer Friendly**: Pre-commit hooks, automated formatting, linting
- **Security First**: Dependency scanning, security analysis, SBOM generation
- **CLI Tool**: Command-line interface via my_python_project

## Quick Start

### Prerequisites

- Python 3.10+ (tested with 3.12)
- [UV](https://docs.astral.sh/uv/) for dependency management

**Install UV**:

```bash
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip/pipx
pip install uv
# or
pipx install uv
```

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/my_python_project.git
cd my_python_project

# Install dependencies
uv sync

# Install with dev tools (recommended)
uv sync --all-extras

# Setup pre-commit hooks (required)
uv run pre-commit install
```

### Basic Usage

```python
# Import and use the package
from my_python_project import YourModule

# Example: Create an instance and use it
module = YourModule()
result = module.process()
print(result)
```

### CLI Usage

```bash
# Display help
uv run my_python_project --help

# Use the CLI tool
uv run my_python_project command --option value

# Example: Process input file
uv run my_python_project process input.txt --output result.json
```

## Google Assured OSS Integration

This project uses **Google Assured OSS** as the primary package source, with PyPI as a fallback. Assured OSS provides vetted, secure open-source packages with Google's security guarantees.

### Why Assured OSS?

- **Security**: All packages are scanned and verified by Google
- **Supply Chain Protection**: Reduced risk of malicious packages
- **Compliance**: Meets enterprise security requirements
- **Automatic Fallback**: Seamlessly falls back to PyPI when needed

### Setup Instructions

1. **Copy the environment template**:
   ```bash
   cp .env.example .env
   ```

2. **Configure Google Cloud Project**:
   ```bash
   # Edit .env and set your GCP project ID
   GOOGLE_CLOUD_PROJECT=your-gcp-project-id
   ```

3. **Setup Authentication** (choose one method):

   **Option A: Service Account JSON File** (local development)
   ```bash
   # Download service account key from GCP Console
   # Set the file path in .env
   GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account-key.json
   ```

   **Option B: Base64 Encoded Credentials** (CI/CD recommended)
   ```bash
   # Encode your service account JSON
   base64 -w 0 service-account-key.json

   # Set the base64 string in .env
   GOOGLE_APPLICATION_CREDENTIALS_B64=<paste-base64-here>
   ```

4. **Validate Configuration**:
   ```bash
   # Run the validation script
   uv run python scripts/validate_assuredoss.py

   # Or use nox
   nox -s assuredoss
   ```

### Service Account Permissions

Your service account needs the following IAM role:
- `roles/artifactregistry.reader` (Artifact Registry Reader)

### Disabling Assured OSS

To use only PyPI (not recommended for production):

```bash
# In .env file
USE_ASSURED_OSS=false
```

### Troubleshooting

**Q: Packages not found in Assured OSS?**
- UV automatically falls back to PyPI for packages not in Assured OSS
- No action needed - this is expected behavior

**Q: Authentication errors?**
- Verify your service account has Artifact Registry Reader role
- Check that GOOGLE_CLOUD_PROJECT is set correctly
- Ensure credentials file/base64 is valid JSON

**Q: How to see which packages are available?**
- Run `nox -s assuredoss` to list all available packages
- Visit: https://cloud.google.com/assured-open-source-software/docs/supported-packages

## Development

### Setup Development Environment

```bash
# Install all dependencies including dev tools
uv sync --all-extras

# Setup pre-commit hooks
uv run pre-commit install

# Install Qlty CLI for unified code quality checks
curl https://qlty.sh | bash

# Run tests
uv run pytest -v

# Run with coverage
uv run pytest --cov=my_python_project --cov-report=html

# Run all quality checks (using Qlty)
qlty check

# Or use pre-commit
uv run pre-commit run --all-files
```

### Code Quality Standards

All code must meet these requirements:

- **Formatting**: Ruff (88 char limit)
- **Linting**: Ruff with comprehensive rules
- **Type Checking**: MyPy strict mode
- **Testing**: Pytest with 60%+ coverage
- **Security**: Bandit + dependency scanning
- **Documentation**: Docstrings on all public APIs

**Unified Quality Tool**: This project uses [Qlty](https://qlty.sh) to consolidate all quality checks into a single fast tool. See [`.qlty/qlty.toml`](.qlty/qlty.toml) for configuration.

### Claude Code Standards

This project includes standardized Claude Code configuration via git subtree:

**Directory Structure**:
```
.claude/
├── claude.md          # Project-specific Claude guidelines
└── standard/          # Standard Claude configuration (git subtree)
    ├── CLAUDE.md      # Universal development standards
    ├── commands/      # Custom slash commands
    ├── skills/        # Reusable skills
    └── agents/        # Specialized agents
```

**Updating Standards**:
```bash
# Pull latest standards from upstream
./scripts/update-claude-standards.sh

# Or manually
git subtree pull --prefix .claude/standard \
    https://github.com/williaby/.claude.git main --squash
```

**What's Included**:
- Universal development best practices
- Response-Aware Development (RAD) system for assumption tagging
- Agent assignment patterns and workflow
- Security requirements and pre-commit standards
- Git workflow and commit conventions

**Project-Specific Overrides**: Edit `.claude/claude.md` for project-specific guidelines. See [`.claude/README.md`](.claude/README.md) for details.

### Running Tests

```bash
# Run all tests
uv run pytest -v

# Run specific test file
uv run pytest tests/unit/test_module.py -v

# Run with coverage report
uv run pytest --cov=my_python_project --cov-report=term-missing

# Run tests in parallel
uv run pytest -n auto
```

### Quality Checks with Qlty

**Recommended**: Use Qlty CLI for unified code quality checks.

```bash
# Run all quality checks (fast!)
qlty check

# Run checks on only changed files (fastest)
qlty check --filter=diff

# Run specific plugins only
qlty check --plugin ruff --plugin mypy

# Auto-format code
qlty fmt

# View current configuration
qlty config show
```

**Qlty runs all these tools in a single pass:**

**Python Quality:**

- Ruff (linting + formatting)
- Mypy (type checking)
- Bandit (security scanning)

**Security & Secrets:**

- Gitleaks (secrets detection)
- TruffleHog (entropy-based secrets detection)
- OSV Scanner (dependency vulnerabilities)
- Semgrep (advanced SAST)

**File & Configuration:**

- Markdownlint (markdown linting)
- Yamllint (YAML linting)
- Prettier (JSON, YAML, Markdown formatting)
- Actionlint (GitHub Actions workflows)
- Shellcheck (shell script linting)

**Container & Infrastructure** (if Docker enabled):

- Hadolint (Dockerfile linting)
- Trivy (container security scanning)
- Checkov (infrastructure as code security)

**Code Quality Metrics:**

- Complexity analysis (cyclomatic, cognitive)
- Code smells detection
- Maintainability scoring

### Individual Tool Commands (if needed)

```bash
# Format code
uv run ruff format src tests

# Lint and auto-fix
uv run ruff check --fix src tests

# Type checking
uv run mypy src

# Security scanning
uv run bandit -r src

# Dependency vulnerabilities
qlty check --plugin osv_scanner
```

## Project Structure

```
my_python_project/
├── src/my_python_project/     # Main package
│   ├── __init__.py
│   ├── core.py                           # Core functionality
│   └── utils/                            # Utility modules
├── tests/                                # Test suite
│   ├── unit/                             # Unit tests
│   └── integration/                      # Integration tests
├── docs/                                 # Documentation
│   ├── ADRs/                             # Architecture Decision Records
│   ├── planning/                         # Project planning docs
│   └── guides/                           # User guides
├── pyproject.toml                        # Dependencies & tool config
├── README.md                             # This file
├── CONTRIBUTING.md                       # Contribution guidelines
└── LICENSE                               # License
```

## Documentation

- **[CONTRIBUTING.md](CONTRIBUTING.md)**: How to contribute to the project
- **[docs/ADRs/README.md](docs/ADRs/README.md)**: Architecture Decision Records documentation
- **[docs/planning/project-plan-template.md](docs/planning/project-plan-template.md)**: Project planning guide

### Writing Documentation

- Use Markdown for all documentation
- Include code examples for clarity
- Update README.md when adding major features
- Maintain architecture documentation (see [docs/ADRs/](docs/ADRs/))

## Testing

### Testing Policy

All new functionality must include tests:

- **Unit tests**: Test individual functions/classes
- **Integration tests**: Test component interactions
- **Coverage**: Maintain 60%+ coverage
- **Markers**: Use pytest markers (`@pytest.mark.unit`, `@pytest.mark.integration`)

### Test Guidelines

```bash
# Run all tests
uv run pytest -v

# Run only unit tests
uv run pytest -v -m unit

# Run only integration tests
uv run pytest -v -m integration

# Run with coverage requirements
uv run pytest --cov=my_python_project --cov-fail-under=60
```

## Security

### Security-First Development

- Validate all inputs
- Use secure defaults
- Scan dependencies regularly
- Report vulnerabilities responsibly

### Reporting Security Issues

Please report security vulnerabilities to you@example.com rather than using the public issue tracker.

See the [yourusername Security Policy](https://github.com/yourusername/.github/blob/main/SECURITY.md) for complete disclosure policy and response timelines.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:

- Development setup
- Code quality standards
- Testing requirements
- Git workflow and commit conventions
- Pull request process

### Quick Checklist Before Submitting PR

- [ ] Code follows style guide (Ruff format + lint)
- [ ] All tests pass with 60%+ coverage
- [ ] MyPy type checking passes
- [ ] Docstrings added for new public APIs
- [ ] CHANGELOG.md updated (if significant change)
- [ ] Commits follow conventional commit format

## Versioning

This project uses [Semantic Versioning](https://semver.org/):

- **MAJOR** version: Incompatible API changes
- **MINOR** version: Backwards-compatible functionality additions
- **PATCH** version: Backwards-compatible bug fixes

Current version: **0.1.0**

## License

MIT License - see [LICENSE](LICENSE) for details.

## Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/my_python_project/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/my_python_project/discussions)
- **Email**: you@example.com

## Acknowledgments

Thank you to all contributors and the open-source community!

---

**Made with by [Your Name](https://github.com/yourusername)**
