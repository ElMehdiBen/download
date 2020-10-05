import subprocess

link = "http://download.companieshouse.gov.uk/BasicCompanyDataAsOneFile-2020-10-01.zip"

filename = link.split("/")[-1]

command = 'curl -o ' + filename + ' ' + link

status, output = subprocess.getstatusoutput(command)