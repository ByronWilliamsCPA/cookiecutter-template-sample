# Claude Code Project Guidelines

> **Standard Guidelines**: See [./standard/claude.md](./standard/claude.md) for:
> - Universal development standards and best practices
> - Response-Aware Development (RAD) system and assumption tagging
> - Agent assignment patterns and workflow
> - Security requirements and pre-commit checks
> - Git workflow and commit conventions
>
> **User Settings**: Global Claude configuration at `~/.claude/CLAUDE.md` (user-level)
>
> This file contains **project-specific** configurations that extend the standard guidelines.

---

## Project Overview

**Name**: My Python Project
**Description**: A short description of the project
**Author**: Your Name <you@example.com>
**Repository**: https://github.com/yourusername/my_python_project

## Technology Stack

- **Python**: 3.12
- **Package Manager**: UV
- **Code Quality**: Ruff (linter/formatter), MyPy (type checker)
- **Testing**: pytest, coverage
- **Security**: Bandit, Safety
- **CLI Framework**: Click
- **Documentation**: MkDocs Material
## Project-Specific Requirements

> **Standard Requirements**: See [./standard/claude.md](./standard/claude.md) for universal standards

**Coverage & Quality**:
- Test coverage: Minimum 60%
- All linters must pass: `uv run ruff check .`, `uv run mypy src/`
- Security scans: `uv run bandit -r src`, `uv run safety check`

## Quick Start Commands

```bash
# Initial setup
uv sync --all-extras
uv run pre-commit install

# Development cycle
uv run pytest -v                           # Run tests
uv run pytest --cov=src --cov-report=html # With coverage
uv run ruff format .                       # Format code
uv run ruff check . --fix                  # Lint and fix
uv run mypy src/                           # Type check

# Before commit (all must pass)
uv run pytest --cov=src --cov-fail-under=60
uv run ruff check .
uv run mypy src/
uv run bandit -r src
pre-commit run --all-files

# Documentation
uv run mkdocs serve                        # Local preview
uv run mkdocs build                        # Build static site
```

## Project Structure

```
src/my_python_project/
├── __init__.py              # Package initialization
├── cli.py                   # CLI entry point
├── core/                    # Core business logic
│   ├── __init__.py
│   └── config.py           # Configuration (Pydantic Settings)
├── middleware/              # Middleware components
│   └── __init__.py
└── utils/                   # Utilities
    ├── __init__.py
    ├── financial.py        # Financial utilities (Decimal precision)
    └── logging.py          # Structured logging

tests/
├── unit/                   # Unit tests
├── integration/            # Integration tests
├── conftest.py            # Pytest fixtures
└── test_example.py        # Example tests

docs/                       # MkDocs documentation
├── index.md               # Home page
└── ...                    # Additional docs
```

## Code Conventions

> **Standard Conventions**: See [./standard/claude.md](./standard/claude.md) for universal naming and style guidelines

**Project-Specific Patterns**:
- Configuration: Use Pydantic Settings with `.env` files
- Logging: Structured logging via `src/my_python_project/utils/logging.py`
- Error Handling: Custom exceptions in `src/my_python_project/core/exceptions.py`

**Docstrings** (Google Style):
```python
def process_data(input_path: str, max_rows: int = 1000) -> dict[str, Any]:
    """Process data from input file.

    Args:
        input_path: Path to input file
        max_rows: Maximum rows to process (default: 1000)

    Returns:
        Dictionary with processing results

    Raises:
        FileNotFoundError: If input file doesn't exist
        ValueError: If file format is invalid
    """
```

## Configuration Management

Use Pydantic Settings for environment-based configuration:

```python
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    project_name: str = "My Python Project"
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    debug: bool = Field(default=False, env="DEBUG")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
```

## Common Tasks

### Add Dependency
```bash
uv add package-name              # Production
uv add --dev package-name        # Development
```

### Update Dependencies
```bash
uv sync --upgrade                        # All packages
uv sync --upgrade-package package-name   # Specific package
```

### Run Specific Test
```bash
uv run pytest tests/unit/test_example.py::test_function_name -v
```

## CI/CD Pipeline

**GitHub Actions Workflows**:
1. **CI** (`.github/workflows/ci.yml`): Tests, linting, type checking
2. **Security** (`.github/workflows/security-analysis.yml`): CodeQL, Bandit, Safety
3. **Docs** (`.github/workflows/docs.yml`): Build and deploy documentation
4. **Publish** (`.github/workflows/publish-pypi.yml`): PyPI release automation

**Quality Gates** (must pass):
- ✅ All tests pass (60% coverage)
- ✅ Ruff linting (no errors)
- ✅ MyPy type checking
- ✅ Security scans (no high/critical)
- ✅ Pre-commit hooks
## Troubleshooting

### Pre-commit Hooks Failing
```bash
pre-commit run --all-files           # Run manually
pre-commit clean                     # Clean cache
pre-commit install --install-hooks   # Reinstall
```

### UV Lock Issues
```bash
uv lock                          # Regenerate lock
uv sync                          # Reinstall dependencies
```

### MyPy Type Errors
```bash
uv run mypy src/ --show-error-codes  # Show error codes
# Add `# type: ignore[error-code]` for specific issues
```

## Performance Targets

| Metric | Target | Notes |
|--------|--------|-------|
| Test Suite | <30s | Full suite with coverage |
| CI Pipeline | <5min | All checks |
| Code Coverage | 60% | Enforced in CI |

## Additional Resources

- **Project README**: [../README.md](../README.md)
- **Contributing Guide**: [../CONTRIBUTING.md](../CONTRIBUTING.md)
- **Security Policy**: [../SECURITY.md](../SECURITY.md)
- **Standard Claude Guidelines**: [./standard/claude.md](./standard/claude.md)
- **UV Documentation**: https://docs.astral.sh/uv/
- **Ruff Documentation**: https://docs.astral.sh/ruff/

---

**Last Updated**: 2025-11-21
**Template Version**: 0.1.0
