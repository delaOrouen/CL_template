#! /bin/bash

if [ $# -ne 0 ]; then
  printf "You need to provide 0 arguments\n"
  printf "Rerun and try again\n"
  exit 1;
fi

printf "New Letter!\n"

python3.9 make_letter.py

lualatex cover_letter_template.tex # Complile the pdf
