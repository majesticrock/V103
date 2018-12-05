all: build/main.pdf

# hier Python-Skripte:
build/stab1_1_dual.pdf: plot-stab1_1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot-stab1_1.py

build/stab1_2_dual.pdf: plot-stab1_2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot-stab1_2.py

build/stab2_single.pdf: plot-stab2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot-stab2.py

build/stab3_single.pdf: plot-stab3.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python plot-stab3.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/stab1_1_dual.pdf build/stab1_2_dual.pdf build/stab2_single.pdf build/stab3_single.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
