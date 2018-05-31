import pandas
import re
import requests
import shutil
import time

INFILE = 'envoynda.xlsx'
COLUMNNAME = 'nda_pdf_url'
PATTERN = "[a-zA-Z0-9-_.%]*.pdf"

excelHandle = pandas.read_excel(INFILE, sheet_name=0)
excelList = excelHandle[COLUMNNAME].tolist()

for fileURL in excelList:
    if fileURL is not None:
        fileName = re.search(PATTERN, fileURL).group(0)
        
        request = requests.get(fileURL, stream=True)
        if request.status_code == 200:
            with open(fileName, 'wb') as outFile:
                request.raw.decode_content = True
                shutil.copyfileobj(request.raw, outFile)
                time.sleep(1)