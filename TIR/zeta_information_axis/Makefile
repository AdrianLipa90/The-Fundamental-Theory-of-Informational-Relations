PYTHON ?= python3
LATEXMK ?= latexmk

.PHONY: all figures audit test monograph clean

all: test audit monograph

figures:
	PYTHONPATH=src $(PYTHON) scripts/make_figures.py

audit:
	PYTHONPATH=src $(PYTHON) scripts/run_audit.py
	PYTHONPATH=src $(PYTHON) scripts/solve_axis.py --output reports/solver_receipt.json

test:
	PYTHONPATH=src pytest -q

monograph: figures audit
	cd monograph && $(LATEXMK) -xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
	cp monograph/main.pdf monograph/information_spinor_critical_axis.pdf

clean:
	cd monograph && $(LATEXMK) -C main.tex || true
	rm -f monograph/information_spinor_critical_axis.pdf
