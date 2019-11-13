#!\bin\bash
for i in $(ls _*.tex); do
	pdflatex $i
	pdflatex $i
done
