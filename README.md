# Ragify Github Discussions

A project to convert github discussions into Q&A system using ChromaDB, and OpenAI APIs

## Setup

1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd github-discussions-rag
   ```

2. **Initialize the environment and install dependencies**
   ```sh
   make init
   ```

## Running the App

Start the Streamlit app:
```sh
make run
```

## Code Quality

Format and lint the code using [ruff](https://docs.astral.sh/ruff/):
```sh
make ruff
```

## Available Makefile Commands

- `make help` — List available commands
- `make init` — Create virtual environment and install dependencies
- `make run` — Run the Streamlit app
- `make ruff` — Lint and format code with ruff

## Notes

- Ensure you have [uv](https://github.com/astral-sh/uv) installed.
- The app entry point is `src/ui/main.py`.