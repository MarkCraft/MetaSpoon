import argparse
import sys
from colorama import Fore, Style, init
import exiftool

# Initialize colorama
init(autoreset=True)

#Print a pretty banner!
def print_banner():
    print(Fore.CYAN + """
    ███╗   ███╗███████╗████████╗ █████╗     ███████╗██████╗  ██████╗  ██████╗ ███╗   ██╗
    ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗    ██╔════╝██╔══██╗██╔═══██╗██╔═══██╗████╗  ██║
    ██╔████╔██║█████╗     ██║   ███████║    ███████╗██████╔╝██║   ██║██║   ██║██╔██╗ ██║
    ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║    ╚════██║██╔═══╝ ██║   ██║██║   ██║██║╚██╗██║
    ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║    ███████║██║     ╚██████╔╝╚██████╔╝██║ ╚████║
    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝    ╚══════╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝
                                                                                      
    """)
    print(Fore.GREEN + "Author: Mark Craft\n")
    print(Fore.YELLOW + "Version: 1.0.0\n")

# Get URLs for the specified parameters. Lists the URLs in a file called urls.txt
def get_urls():

    query = "site:*.org filetype:pdf"
    all_links = []

# Downloads all of the files from a file of valid URLs
def dowload_files():

    count = 0

test = exiftool

""" 
Possible command and options:

dork, dork and scrape public facing documents, all urls will be placed into a file called [domain]-urls.txt in the working directory.
All files will then be downloaded into a folder called files.
-d, --domain, domain/site to dork 
-f, --filetype, file type extension to search for. Multiple types can be used. If not used, default will look for all extensions.
Extensions include: pdf, doc, docx, xls, xlsx, ppt, pptx, txt, conf, log, xml, jpg, jpeg, png, mp3, mp4
-l, --limit, limit the number of results returned, retreive the first l results 
-h, --help, help for using the dork command

analyze, analyze metadata for a specific file, list of files or all files within a directory, exiftool will pull this metadata

-f, --file, file to analyze
-d, --directory, directory of files to analyze
-o, --output, output metada into both a txt file and a csv file. Analyze will command will read from the csv file
-t, --tags, returns all unique metadata tags in a csv file
-u, --value, returns all unique values given a valid metadata tag, if multiple files exist in the csv, the filename will be included
-h, --help, help for using the analyze command

"""


def main():

    print_banner()

main()
