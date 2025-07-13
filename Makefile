help:
	@echo "Available targets:"
	@echo "  init   - Create virtual environment and install dependencies"
	@echo "  run    - Run the Streamlit app"

init:
	uv venv
	uv sync

run:
	export PYTHONPATH=.
	uv run streamlit run src/ui/main.py

ruff:
	uv run ruff check --fix
	uv run ruff format