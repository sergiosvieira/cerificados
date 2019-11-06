all:
	python main.py
	sh pdf.sh
clean:
	rm -f _*.tex
	rm -f *.aux
	rm -f *.log
	rm -f *.pdf
