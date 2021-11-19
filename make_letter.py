import pathlib

company_name = input("Enter the company name: ")
recipient_address = 'Dear ' + company_name + ',\\newline \n \\newline '
letter_body = "Words words words words words words words words words words words words words words words. " \
                "Words words words words words words words. Words words words words words words words words words " \
                "words words words words words."
entire_letter = recipient_address + letter_body

path_string = "/home/tatsuya/Documents/CL_template/my_letter.tex"
path = pathlib.Path(path_string)
path.unlink(missing_ok=True) # this deletes my_letter.tex if it exists

outputFile = open(path_string, "w")
outputFile.write(entire_letter)
outputFile.close()


