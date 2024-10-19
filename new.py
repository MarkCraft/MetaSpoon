import argparse
import sys
from colorama import Fore, Style, init

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
def dowload_urls():

    count = 0


""" 
Possible arguments:
-d, --domain, domain/site to dork
-t, --type, file type to search for. 
"""


def main():

    print_banner()

main()
