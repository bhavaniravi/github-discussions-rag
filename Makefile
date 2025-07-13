init:
	uv venv
	uv sync

run:
	export PYTHONPATH=.
	uv run 