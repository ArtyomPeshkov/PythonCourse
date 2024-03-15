Docker is located in src.
Docker copy:
$
FROM ubuntu:latest

RUN apt-get update && apt-get install -y texlive-latex-base

COPY test.tex /app/
ADD resources /app/resources/
WORKDIR /app

CMD pdflatex test.tex && cp test.pdf /output/
$