import os
import os.path
import sys 
try:
    from fuzzywuzzy import fuzz
except ImportError:
    print("fuzzywuzzy Is Not Installed, Installing it :)")
    os.system("pip3 install python-Levenshtein fuzzywuzzy")
from colorama import Fore, Back, Style


NitelyPath = sys.argv[0].replace('/NiteylTerminalAdvanced.py', '')
AppNames = []

for AppName in os.listdir(f"{NitelyPath}/apps"):
    if sys.maxsize > 32:
        if os.path.isfile(f"{NitelyPath}/apps/{AppName}/install-32") or os.path.isfile(f"{NitelyPath}/apps/{AppName}/install") and AppName != "template":
            AppNames.append(AppName)
    else:
        if os.path.isfile(f"{NitelyPath}/apps/{AppName}/install-64") or os.path.isfile(f"{NitelyPath}/apps/{AppName}/install") and AppName != "template":
            AppNames.append(AppName)

AppNames.sort()

def list_(Type):
    if Type == 'all':
        for appname in AppNames:
            print(Fore.GREEN + appname)
            descriptionfile = open(f"{NitelyPath}/apps/{appname}/description","r")
            description = descriptionfile.read()
            print(Fore.CYAN + description)
            descriptionfile.close()
    else:
        for InstalledApp in os.listdir(f"{NitelyPath}/data/status"):
            AppStatus = open(f"{NitelyPath}/data/status/{InstalledApp}" ,"r")
            status = AppStatus.read()
            AppStatus.close()
            if status.strip() == Type:
                print(Fore.GREEN + InstalledApp)
                descriptionfile = open(f"{NitelyPath}/apps/{InstalledApp}/description","r")
                description = descriptionfile.read()
                print(Fore.CYAN + description)
                descriptionfile.close()

def install(AppName):
    for App in AppNames:
        if AppName == App:
            os.system(f"{NitelyPath}/manage install '{AppName}'")
            break
    else:
        print(Fore.RED + "App Doesnt Exist. Use command 'nitely list-all' to list the available apps also make sure to use '' while entering app name")

def uninstall(AppName):
    for App in AppNames:
        if AppName == App:
            os.system(f"{NitelyPath}/manage uninstall '{AppName}'")
            break
    else:
        print(Fore.RED + "App Doesnt Exist. Use command 'nitely list-all' to list the available apps also make sure to use '' while entering app name")


def search(AppName):
    SearchResults=0
    SimilarityRubric=100
    if sys.argv[1] == "search":
        while SearchResults==0:
            if SimilarityRubric > 0:
                SimilarityRubric -= 10
                for App in AppNames:
                    similarity= fuzz.ratio(App.lower(), AppName.lower())
                    if similarity > SimilarityRubric or similarity == SimilarityRubric:
                        print(Fore.GREEN + App)
                        fo = open(f"{NitelyPath}/apps/{App}/description","r")
                        description = fo.read()
                        print(Fore.CYAN + description)
                        fo.close()
                        SearchResults += 1
            else:
                print("No Search Results Found :(")
                quit()

def website(AppName):
    AppFound = False
    for App in AppNames:
        if AppName == App:
            WebsiteFile = open(f"{NitelyPath}/apps/{App}/website","r")
            website = WebsiteFile.read()
            print(Fore.CYAN + website.strip())
            WebsiteFile.close()
            AppFound = True
            quit()
    if AppFound == False:
        print(Fore.RED + "Please enter valid appname. Use command 'nitely list-all' to get the list of apps")            
                
def help_():
    print(Fore.BLUE + "Usage")
    print(Fore.GREEN + "nitely [argument]")
    print()
    print(Fore.BLUE + "Available Arguments: ")
    print(Fore.GREEN + "list-all" +Fore.CYAN+ "  Prints the list of available apps that are installable")
    print(Fore.GREEN + "list-installed" +Fore.CYAN+ "  Prints all installed apps")
    print(Fore.GREEN + "list-uninstalled" +Fore.CYAN+ "  Prints all uninstalled apps")
    print(Fore.GREEN + "install '[appname]'" +Fore.CYAN+ "  Install any app available in nitely")
    print(Fore.GREEN + "uninstall '[appname]'" +Fore.CYAN+ "  Uninstall any app available in nitely")
    print(Fore.GREEN + "search '[appname]'" +Fore.CYAN+ "  Search for a app in nitely")
    print(Fore.GREEN + "update" +Fore.CYAN+ "  Update nitely")
    print(Fore.GREEN + "website '[appname]'" +Fore.CYAN+ "  Prints the website for app")
    print(Fore.GREEN + "gui" +Fore.CYAN+ "  Launches gui for nitely")


if len(sys.argv) > 1:
    if sys.argv[1] == 'install':
        if len(sys.argv) > 2:
            install(sys.argv[2])
        else:
            print(Fore.RED + "Enter Valid App Name. Use command 'nitely list-all' to list the apps also make sure to use '' while entering app name if it contains spaces")
    elif sys.argv[1] == 'uninstall':
        if len(sys.argv) > 2:
            uninstall(sys.argv[2])
        else:
            print(Fore.RED + "Enter Valid App Name. Use command 'nitely list-installed' to list the installed apps also make sure to use '' while entering the app name if it contains spaces")
    elif sys.argv[1] == 'website':
        if len(sys.argv) > 2:
            website(sys.argv[2])
        else:
            print(Fore.RED + "Enter Valid App Name. Use command 'nitely list-all' to list the apps also make sure to use '' while entering app name if it contains spaces")
    elif sys.argv[1] == 'search':
        if len(sys.argv) > 2:
            search(sys.argv[2])
        else:
            print(Fore.RED + "Enter valid search term")
    elif sys.argv[1] == 'list-all' or sys.argv[1] == 'list-installed' or sys.argv[1] == 'list-uninstalled':
        list_(sys.argv[1].replace('list-', ''))
    elif sys.argv[1] == 'gui':
        os.system(f"{NitelyPath}/gui &")
    elif sys.argv[1] == 'help':
        help_()
    elif sys.argv[1] == 'update':
        os.system(f"{NitelyPath}/manage update-all")
    else:
        print(Fore.RED + "Please enter valid argument. Use command 'nitely help' to get a list of valid arguments")
        quit()
else:
    os.system(f"{NitelyPath}/gui")
