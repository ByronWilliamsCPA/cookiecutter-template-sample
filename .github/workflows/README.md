# GitHub Actions Workflows

This project uses **org-level reusable workflows** for consistency and maintainability across all yourusername projects.

## Architecture

```
┌─────────────────────────────────────────┐
│  my_python_project        │
│  (This Repository)                      │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Caller Workflows (.github/        │ │
│  │ workflows/*.yml)                   │ │
│  │                                    │ │
│  │ • ci.yml                           │ │
│  │ • security-analysis.yml            │ │
│  │ • docs.yml                         │ │
│  │ • publish-pypi.yml                 │ │
│  │ • release.yml                      │ │
│  └───────────────────────────────────┘ │
│              │                          │
│              │ uses:                    │
│              ▼                          │
└─────────────────────────────────────────┘
               │
               │
┌──────────────▼──────────────────────────┐
│  yourusername  │
│  /.github Repository                    │
│  (Organization-Level)                   │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Reusable Workflows (.github/      │ │
│  │ workflows/*.yml)                   │ │
│  │                                    │ │
│  │ • python-ci.yml                    │ │
│  │ • python-security-analysis.yml     │ │
│  │ • python-docs.yml                  │ │
│  │ • python-publish-pypi.yml          │ │
│  │ • python-release.yml               │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## Workflow Descriptions

### CI Pipeline (`ci.yml`)
**Calls**: `yourusername/.github/.github/workflows/python-ci.yml@main`

Comprehensive CI with:
- Multi-version Python testing (3.12)
- UV dependency management
- Ruff linting and formatting
- MyPy type checking (strict mode)
- Pytest with 60%+ coverage
- Codecov integration

**Triggers**: Push/PR to main branches, manual dispatch

---

### Security Analysis (`security-analysis.yml`)
**Calls**: `yourusername/.github/.github/workflows/python-security-analysis.yml@main`

Comprehensive security scanning with:
- CodeQL advanced analysis
- Bandit static security analysis
- Safety dependency CVE scanning
- OSV Scanner
- OWASP dependency check
- Dependency review (PRs only)

**Triggers**: Push/PR to main, weekly schedule, manual dispatch

---

### Documentation (`docs.yml`)
**Calls**: `yourusername/.github/.github/workflows/python-docs.yml@main`

Documentation build and deployment:
- MkDocs build with Material theme
- Link validation
- Deployment to GitHub Pages (on push to main)

**Triggers**: Push/PR affecting docs, manual dispatch
---

### Publish to PyPI (`publish-pypi.yml`)
**Calls**: `yourusername/.github/.github/workflows/python-publish-pypi.yml@main`

Package publishing with:
- OIDC trusted publishing (no API tokens needed)
- Test PyPI validation
- SBOM generation
- Signed releases

**Triggers**: Release published, manual dispatch

---

### Release (`release.yml`)
**Calls**: `yourusername/.github/.github/workflows/python-release.yml@main`

Release automation with:
- SLSA provenance generation
- Signed artifacts
- Comprehensive changelog
- Asset upload

**Triggers**: Version tags (v*.*.*), manual dispatch

---

## Benefits of Org-Level Reusable Workflows

### ✅ **Consistency**
All projects use the same tested CI/CD pipeline configuration.

### ✅ **Maintainability**
- Update workflows once at org level
- All projects inherit improvements automatically
- No need to update hundreds of project workflows

### ✅ **Reduced Duplication**
- Caller workflows are ~50 lines vs ~300+ for embedded workflows
- 85% reduction in workflow code per project

### ✅ **Version Control**
- Workflows versioned at `@main` (or pin to specific version/SHA)
- Easy rollback if needed

### ✅ **Security**
- Centralized security updates
- Consistent security practices across org

---

## Configuration

Caller workflows are configured via `with:` parameters. See individual workflow files for available options.

Example customization:
```yaml
jobs:
  ci:
    uses: yourusername/.github/.github/workflows/python-ci.yml@main
    with:
      python-versions: '["3.10", "3.11", "3.12"]'  # Test multiple versions
      coverage-threshold: 85                        # Higher threshold
      mypy-strict: true                             # Strict type checking
```

---

## Local Development

Workflows can be tested locally using [act](https://github.com/nektos/act):

```bash
# Test CI workflow
act -j ci

# Test security workflow
act -j security

# Test with specific event
act push -j ci
```

---

## Troubleshooting

### Workflow Fails to Find Reusable Workflow
**Error**: `Workflow file not found`

**Solution**: Ensure the org-level `.github` repository exists and workflows are at:
```
yourusername/.github/.github/workflows/*.yml
```

### Permission Denied
**Error**: `Resource not accessible by integration`

**Solution**: Check workflow permissions. Caller workflows inherit permissions from reusable workflows, but may need additional `permissions:` blocks.

### Secrets Not Available
**Error**: `Secret not found`

**Solution**: Add secrets at repository or organization level:
- Repository Settings → Secrets and variables → Actions
- Organization Settings → Secrets and variables → Actions

---

## Documentation

- [GitHub Reusable Workflows Docs](https://docs.github.com/en/actions/using-workflows/reusing-workflows)
- [Org-Level Workflow Source](https://github.com/yourusername/.github/tree/main/.github/workflows)
- [Project Contributing Guide](../../CONTRIBUTING.md)

---

**Last Updated**: {{ cookiecutter.project_name }} generated from template
**Org Workflows Version**: `@main` (auto-updates with org changes)
