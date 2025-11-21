# Project Setup Guide

This guide covers everything you need to know after generating your project from the cookiecutter template. It includes manual setup steps, keeping your project updated, and managing your repository structure.

## Table of Contents

- [Initial Setup](#initial-setup)
- [Manual Registrations Required](#manual-registrations-required)
- [Keeping Your Project Updated](#keeping-your-project-updated)
- [CI/CD Workflow Configuration](#cicd-workflow-configuration)
- [Badge Configuration](#badge-configuration)
- [Security Configuration](#security-configuration)
- [Repository Management](#repository-management)

---

## Initial Setup

After generating your project, complete these steps:

### 1. Review Generated Files

Your project was generated with the following configuration:

- **Project Name**: My Python Project
- **Python Version**: 3.12
- **License**: MIT

### 2. Create GitHub Repository

```bash
# Create a new repository on GitHub, then:
git remote add origin https://github.com/ByronWilliamsCPA/cookiecutter-template-sample.git
git push -u origin master
```

### 3. Install Dependencies

```bash
# Install UV if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install project dependencies
uv sync --all-extras

# Install pre-commit hooks
uv run pre-commit install
```

### 4. Verify Setup

```bash
# Run tests
uv run pytest -v

# Run linting
uv run ruff check .

# Run type checking
uv run mypy src/
```

---

## Manual Registrations Required

Some features require manual registration on external services:

### OpenSSF Best Practices Badge

The OpenSSF Best Practices badge requires manual project registration:

1. **Register your project**: Visit [https://www.bestpractices.dev/en](https://www.bestpractices.dev/en)
2. **Click "Get Your Badge Now"**
3. **Enter your repository URL**: `https://github.com/ByronWilliamsCPA/cookiecutter-template-sample`
4. **Complete the questionnaire** answering questions about your project's security practices
5. **Get your badge ID** (e.g., `12345`)
6. **Add the badge to your README**:

```markdown
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/YOUR_PROJECT_ID/badge)](https://www.bestpractices.dev/en/projects/YOUR_PROJECT_ID)
```

**Tip**: Many questions can be answered "Met" based on this template's default configuration (CI/CD, security scanning, documentation, etc.).

### Codecov Configuration

1. **Sign up/Login**: Visit [https://codecov.io](https://codecov.io) and authenticate with GitHub
2. **Add repository**: Navigate to your organization and add the repository
3. **Copy the upload token** (optional for public repos, required for private)
4. **Add as GitHub secret**: Repository Settings > Secrets > `CODECOV_TOKEN`

---

## Keeping Your Project Updated

This template uses [Cruft](https://cruft.github.io/cruft/) for template management, allowing you to receive updates.

### Check for Template Updates

```bash
# Check if updates are available
cruft check

# See what would change
cruft diff
```

### Apply Template Updates

```bash
# Update to the latest template version
cruft update

# If there are conflicts, resolve them manually
# Then mark as resolved:
cruft update --skip
```

### Best Practices for Updates

1. **Create a branch** before updating: `git checkout -b template-update`
2. **Review all changes** carefully with `cruft diff`
3. **Test thoroughly** after updating: `uv run pytest && uv run ruff check .`
4. **Commit with clear message**: `git commit -m "chore: update from cookiecutter template"`

### Handling Merge Conflicts

When conflicts occur:

```bash
# After cruft update shows conflicts
git status  # See conflicted files

# Edit files to resolve conflicts
# Then stage resolved files
git add <resolved-files>

# Complete the update
cruft update --skip
```

---

## CI/CD Workflow Configuration

Your project includes several GitHub Actions workflows:

### Core Workflows

| Workflow | File | Purpose |
|----------|------|---------|
| CI Pipeline | `ci.yml` | Tests, linting, type checking |
| Security Analysis | `security-analysis.yml` | Dependency scanning, CodeQL |
| OpenSSF Scorecard | `scorecard.yml` | Supply chain security assessment |
| SBOM & Security Scan | `sbom.yml` | Software Bill of Materials generation |
| Documentation | `docs.yml` | Build and deploy MkDocs |

### Required GitHub Secrets

Set these in Repository Settings > Secrets and variables > Actions:

| Secret | Required For | How to Get |
|--------|--------------|------------|
| `CODECOV_TOKEN` | Codecov uploads | codecov.io > Settings > Upload Token |
| `SCORECARD_TOKEN` | Scorecard (optional) | GitHub PAT with repo scope |

---

## Badge Configuration

### Automatic Badges (No Setup Required)

These badges work automatically once your repository is public:

- **OpenSSF Scorecard**: Updates weekly after first workflow run
- **CI Pipeline**: Shows status after first push
- **Security Analysis**: Shows status after first push
- **SBOM & Security Scan**: Shows status after dependency changes

### Badges Requiring Registration

| Badge | Service | Registration URL |
|-------|---------|-----------------|
| OpenSSF Best Practices | bestpractices.dev | [Register Project](https://www.bestpractices.dev/en) |
| Codecov | codecov.io | [Add Repository](https://codecov.io) |

### Adding OpenSSF Best Practices Badge

After registration, add this badge to your README's "Quality & Security" section:

```markdown
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/YOUR_ID/badge)](https://www.bestpractices.dev/en/projects/YOUR_ID)
```

---

## Security Configuration

### Branch Protection Rules

Enable these on your default branch:

1. Go to Repository Settings > Branches > Add rule
2. Apply to: `master` (or `main`)
3. Enable:
   - [x] Require a pull request before merging
   - [x] Require status checks to pass
   - [x] Require branches to be up to date
   - [x] Include administrators

### Required Status Checks

Add these as required checks:
- `test` (from CI workflow)
- `lint` (from CI workflow)
- `codecov/patch`

### Security Policy

Your `SECURITY.md` file is already configured. Update these sections:

1. **Supported Versions**: Update as you release new versions
2. **Security Contact**: Change the contact email if needed
3. **PGP Key**: Add your security team's PGP key for encrypted reports

---

## Repository Management

### Release Process

1. **Update version** in `pyproject.toml`
2. **Update CHANGELOG.md** with release notes
3. **Create a tag**:
   ```bash
   git tag -a v1.0.0 -m "Release v1.0.0"
   git push origin v1.0.0
   ```
4. **Create GitHub Release** from the tag

### Dependency Updates

Renovate is configured to automatically create PRs for dependency updates. Review and merge these regularly.

### Code Quality Standards

This project enforces:

- **80%+ test coverage** (enforced via pytest-cov)
- **Zero linting errors** (enforced via Ruff)
- **Type safety** (enforced via MyPy)
- **Security scanning** (enforced via Bandit, Safety)

### Project Structure

```
my_python_project/
├── src/my_python_project/    # Main package
│   ├── core/                 # Core functionality
│   ├── utils/                # Utility functions
│   └── cli.py                # CLI entrypoint
├── tests/                    # Test suite
├── docs/                     # Documentation
├── .github/workflows/        # CI/CD workflows
├── pyproject.toml            # Project configuration
└── README.md                 # Project readme
```

---

## Getting Help

- **Template Issues**: [cookiecutter-python-template issues](https://github.com/ByronWilliamsCPA/cookiecutter-python-template/issues)
- **Cruft Documentation**: [cruft.github.io/cruft](https://cruft.github.io/cruft/)
- **UV Documentation**: [docs.astral.sh/uv](https://docs.astral.sh/uv/)
- **OpenSSF Scorecard**: [securityscorecards.dev](https://securityscorecards.dev/)
- **OpenSSF Best Practices**: [bestpractices.dev](https://www.bestpractices.dev/)
