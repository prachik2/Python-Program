import pdfcrowd
import sys
import os

try:
    # create the API client instance
	count = 1
	
	client = pdfcrowd.HtmlToPdfClient('gaurita', '33f65d57ef9491d71fc3cf71fdced981')
	
	pdf_output_files = []
	html_input_files_list = [x for x in os.listdir('/home/prachi/Desktop/html_input_files') if x.endswith(".html")]
	for html_file in html_input_files_list :
		pdf_file = client.convertFileToFile('/home/prachi/Desktop/html_input_files/'+html_file , "/home/prachi/Desktop/html_input_files/output/output_{}.pdf".format(count))
		pdf_output_files.append(pdf_file)
		count += 1

except pdfcrowd.Error as why:
    # report the error to the standard error stream
    sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
