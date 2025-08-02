<<<<<<< HEAD
# Contributing to Farmer AI Assistant

Thank you for your interest in contributing to the Farmer AI Assistant project! This document provides guidelines for contributing to the project.

## 🤝 How to Contribute

### 1. Fork the Repository

1. Go to the [Farmer AI Assistant repository](https://github.com/yourusername/farmer-ai-assistant)
2. Click the "Fork" button in the top right corner
3. Clone your forked repository to your local machine

```bash
git clone https://github.com/yourusername/farmer-ai-assistant.git
cd farmer-ai-assistant
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install flake8 black pytest
```

### 3. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 4. Make Your Changes

- Write clean, well-documented code
- Follow the existing code style
- Add tests for new functionality
- Update documentation as needed

### 5. Test Your Changes

```bash
# Run all tests
python test_basic.py
python test_config.py
python test_stt.py
python test_tts.py
python test_ai_model.py

# Run linting
flake8 .
```

### 6. Commit Your Changes

```bash
git add .
git commit -m "feat: add your feature description"
```

### 7. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub.

## 📋 Contribution Guidelines

### Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions small and focused

### Testing

- Write tests for all new functionality
- Ensure all existing tests pass
- Aim for good test coverage

### Documentation

- Update README.md if needed
- Add comments to complex code
- Update API documentation

### Commit Messages

Use conventional commit format:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `test:` for adding tests
- `refactor:` for code refactoring

## 🐛 Reporting Bugs

1. Check if the bug has already been reported
2. Create a new issue with a clear title
3. Provide detailed steps to reproduce the bug
4. Include error messages and logs
5. Specify your environment (OS, Python version, etc.)

## 💡 Suggesting Features

1. Check if the feature has already been suggested
2. Create a new issue with the "enhancement" label
3. Describe the feature and its benefits
4. Explain how it fits into the project's goals

## 🔧 Development Setup

### Prerequisites

- Python 3.8+
- Git
- Twilio Account (for testing)

### Environment Variables

Create a `.env` file for development:

```env
# Twilio Configuration
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=+12182199792

# Development Configuration
DEBUG=True
HOST=localhost
PORT=8000
```

### Running the Application

```bash
# Start the development server
python main.py

# Or using uvicorn
uvicorn main:app --host localhost --port 8000 --reload
```

## 🧪 Testing Guidelines

### Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python test_config.py

# Run with coverage
python -m pytest --cov=.
```

### Writing Tests

- Test both success and failure cases
- Mock external dependencies
- Use descriptive test names
- Group related tests in classes

## 📚 Documentation

### Code Documentation

- Use docstrings for all public functions
- Follow Google docstring format
- Include type hints where possible

### API Documentation

- Update API endpoint documentation
- Include request/response examples
- Document error codes and messages

## 🔒 Security

- Never commit sensitive information (API keys, passwords)
- Use environment variables for configuration
- Follow security best practices
- Report security vulnerabilities privately

## 📞 Getting Help

- Check existing issues and discussions
- Join our community chat
- Contact the maintainers directly

## 🙏 Recognition

Contributors will be recognized in:

- README.md contributors section
- Release notes
- Project documentation

## 📝 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

=======
# Contributing to Farmer AI Assistant

Thank you for your interest in contributing to the Farmer AI Assistant project! This document provides guidelines for contributing to the project.

## 🤝 How to Contribute

### 1. Fork the Repository

1. Go to the [Farmer AI Assistant repository](https://github.com/yourusername/farmer-ai-assistant)
2. Click the "Fork" button in the top right corner
3. Clone your forked repository to your local machine

```bash
git clone https://github.com/yourusername/farmer-ai-assistant.git
cd farmer-ai-assistant
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install flake8 black pytest
```

### 3. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 4. Make Your Changes

- Write clean, well-documented code
- Follow the existing code style
- Add tests for new functionality
- Update documentation as needed

### 5. Test Your Changes

```bash
# Run all tests
python test_basic.py
python test_config.py
python test_stt.py
python test_tts.py
python test_ai_model.py

# Run linting
flake8 .
```

### 6. Commit Your Changes

```bash
git add .
git commit -m "feat: add your feature description"
```

### 7. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub.

## 📋 Contribution Guidelines

### Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions small and focused

### Testing

- Write tests for all new functionality
- Ensure all existing tests pass
- Aim for good test coverage

### Documentation

- Update README.md if needed
- Add comments to complex code
- Update API documentation

### Commit Messages

Use conventional commit format:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `test:` for adding tests
- `refactor:` for code refactoring

## 🐛 Reporting Bugs

1. Check if the bug has already been reported
2. Create a new issue with a clear title
3. Provide detailed steps to reproduce the bug
4. Include error messages and logs
5. Specify your environment (OS, Python version, etc.)

## 💡 Suggesting Features

1. Check if the feature has already been suggested
2. Create a new issue with the "enhancement" label
3. Describe the feature and its benefits
4. Explain how it fits into the project's goals

## 🔧 Development Setup

### Prerequisites

- Python 3.8+
- Git
- Twilio Account (for testing)

### Environment Variables

Create a `.env` file for development:

```env
# Twilio Configuration
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=+12182199792

# Development Configuration
DEBUG=True
HOST=localhost
PORT=8000
```

### Running the Application

```bash
# Start the development server
python main.py

# Or using uvicorn
uvicorn main:app --host localhost --port 8000 --reload
```

## 🧪 Testing Guidelines

### Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python test_config.py

# Run with coverage
python -m pytest --cov=.
```

### Writing Tests

- Test both success and failure cases
- Mock external dependencies
- Use descriptive test names
- Group related tests in classes

## 📚 Documentation

### Code Documentation

- Use docstrings for all public functions
- Follow Google docstring format
- Include type hints where possible

### API Documentation

- Update API endpoint documentation
- Include request/response examples
- Document error codes and messages

## 🔒 Security

- Never commit sensitive information (API keys, passwords)
- Use environment variables for configuration
- Follow security best practices
- Report security vulnerabilities privately

## 📞 Getting Help

- Check existing issues and discussions
- Join our community chat
- Contact the maintainers directly

## 🙏 Recognition

Contributors will be recognized in:

- README.md contributors section
- Release notes
- Project documentation

## 📝 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

>>>>>>> e15bec281abf2b62dc4fb58236aef25909e43dfc
Thank you for contributing to Farmer AI Assistant! 🌾 