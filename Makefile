test:
	uv run pytest

test_headed:
	uv run pytest --headed

test_parallel:
	uv run pytest --numprocesses 4

test_codegen:
	uv run playwright codegen

test_install:
	uv run playwright install