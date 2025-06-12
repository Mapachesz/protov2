.PHONY: pycompile

# Compile all Python files to check syntax errors
pycompile:
	python -m py_compile *.py
