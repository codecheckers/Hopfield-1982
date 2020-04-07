default: codecheck

codecheck:
	rm -f *.pdf
	cp ../code/*.py .
	python Hopfield-1982.py
	rm *.py
	rm -r __pycache__

codecheck.pdf: codecheck.Rmd codecheck
	Rscript -e 'rmarkdown::render("$<")'
