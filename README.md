# Math Ops

This repository is created for students to practice software development using Python. It focuses on applying the following principles:

- **Test-Driven Development (TDD)**: Writing tests before implementing code.
- **Package Management**: Managing dependencies and packaging Python projects effectively.
- **Git Flow**: Using branches and workflows to manage feature development and releases.

## Tools and Practices

To ensure high-quality code and maintainable projects, the repository also encourages the use of the following tools:

- **Linting**: Tools like `pylint` are used to enforce coding standards and catch potential errors early.
- **Formatting**: Tools like `black` or `autopep8` are used to maintain consistent code formatting.
- **Testing**: `pytest` is used for writing and running test cases.
- **Version Control**: Git is used for source control, adhering to the principles of Git Flow for managing branches and releases.
- **Dependency Management**: Managed through Poetry for an efficient and reproducible development environment.
- **Pre-Commit Hooks**: Tools like `pre-commit` are integrated to automate checks (e.g., linting, formatting) before committing changes.

## Getting Started

1. Clone the repository:

   ```bash
   git clone git@github.com:kebrahimpour/math-ops.git
   cd math-ops

2. Install dependencies:

    poetry install

3. Run tests:
    poetry run pytest

4. Format code:
    poetry run black .

5. Lint code:
    poetry run pylint math_ops tests

## Contribution Guidelines

 • Follow TDD principles when contributing new features.
 • Ensure all changes pass linting and formatting checks before committing.
 • Use branches to manage new features, adhering to Git Flow practices.
 • Submit pull requests for review.

1. Edit your `README.md` file:

   ```bash
   nano README.md

2. Add the updated content.

3. Commit and push the changes


## Development Workflow

### Linting with pylint
    poetry run pylint libs src

### Formatting with black
    poetry run black .

### Auto-format specific files:
    poetry run black path/to/file.py

### Pre-commit Hooks
#### Run hooks manually
    poetry run pre-commit run --all-files


### poetry run pytest
    poetry run pytest

### Run specific tests:
    poetry run pytest path/to/test_file.py
