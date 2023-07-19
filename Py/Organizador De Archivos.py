from os import mkdir, listdir
from os.path import exists, isfile
from shutil import move, Error
from argparse import ArgumentParser
try:
    from colorama import init
except ModuleNotFoundError:
    """
        If the colorama module is not installed, it will be installed below:
    """
    from os import system
    print("[!] It seems you do not have colorama installed, now we will install it for you")
    print("[!] Through a \"pip install colorama\"")
    system("pip install colorama")
    from colorama import init
    
    
    
init() # start colorama

class COLOR:
          
    def __init__(self):
       
        self.BLACK           =  "\033[30m"
        self.RED             =  "\033[31m"
        self.GREEN           =  "\033[32m"
        self.YELLOW          =  "\033[33m"
        self.BLUE            =  "\033[34m"
        self.MAGENTA         =  "\033[35m"
        self.CYAN            =  "\033[36m"
        self.WHITE           =  "\033[37m"
        self.RESET           =  "\033[39m"

        self.LIGHTBLACK_EX   =  "\033[90m"
        self.LIGHTRED_EX     =  "\033[91m"
        self.LIGHTGREEN_EX   =  "\033[92m"
        self.LIGHTYELLOW_EX  =  "\033[93m"
        self.LIGHTBLUE_EX    =  "\033[94m"
        self.LIGHTMAGENTA_EX =  "\033[95m"
        self.LIGHTCYAN_EX    =  "\033[96m"
        self.LIGHTWHITE_EX   =  "\033[97m"

    def UP(self, n=1):
        return '\033[' + str(n) + 'A'
    def DOWN(self, n=1):
        return '\033[' + str(n) + 'B'
    def FORWARD(self, n=1):
        return '\033[' + str(n) + 'C'
    def BACK(self, n=1):
        return '\033[' + str(n) + 'D'
    def POS(self, x=1, y=1):
        return '\033[' + str(y) + ';' + str(x) + 'H'
    def SET_TITLE(self, text):
        return "\033]2;{}\007".format(text)
    def CLEAR(self):
        return "\033[3J\033[H\033[2J"
    def POINTGREEN(self, text1="", text2=""):
        return self.LIGHTGREEN_EX+"["+self.BLUE+"*"+self.LIGHTGREEN_EX+"] "+self.LIGHTWHITE_EX+text1+text2+self.LIGHTWHITE_EX
    def POINTRED(self, text=""):
        return self.LIGHTYELLOW_EX+"["+self.RED+"*"+self.LIGHTYELLOW_EX+"] "+self.LIGHTMAGENTA_EX+text+"\n"+self.LIGHTWHITE_EX



__version__ =  1.0
__autor__   =  "VictorCast2"
__github__  =  "https://github.com/VictorCast2/?tab=File-Organizer"
__doc__     =  "Script to organize files in different "
__doc__    +=  "Folders according to the extension they have"


def create_folders_if_not_exist(carpetas, ruta="C:\Users\casti\Videos"):
    """
        This function receives in the form of a list, the folders to create
         if they don't exist Usage example:

             folders = ["documents", "photos"]
             create_folders_if_doesn't_exist(folders)

         This checks if the documents folder and the photos folder exist,
         otherwise, create it
    """
    _COLOR = COLOR()
    BannerInformativo = "{}[{}*{}] {}".format(_COLOR.LIGHTGREEN_EX, _COLOR.LIGHTRED_EX, _COLOR.LIGHTGREEN_EX, _COLOR.LIGHTYELLOW_EX)
    for carpeta in carpetas:
        if exists(ruta+carpeta) != True:
            ## If the folder does not exist exists() returns False which is different from True.
            ## and this condition will be carried out.
            mkdir(ruta+carpeta)
            print("{} Creating the folder -> {}".format(BannerInformativo, carpeta))
    """
        # This code snippet has been optimized before:
        if exists("documentos") == True: 
            pass
        else: 
            mkdir("documentos")
            continue
        if exists("fotos") == True: pass
        else:
            mkdir("fotos") 
            continue
        if exists("videos") == True:
            pass
        else:
            mkdir("videos")
            continue
        if exists("otros") == True:
            pass
        else:
            mkdir("videos")
            continue
        if exists("musica") == True:
            pass
        else:
            mkdir("musica")
        break
    """

def associate_folders_with_extensions(nombre_carpeta, extensiones_de_archivos, ruta="C:\Users\casti\Videos", ArchivosExcepciones=[]):
    """
         This function receives a tuple in the file_extensions argument.
         containing the extensions of the files you want
         save to the folder specified in the folder_name argument.
         folder_name is an argument of type string(str), this value must be the name
         of the folder to which the extensions will be associated. Optionally you can
         specify the path to work with, with the path argument, which must be a string.
         Usage example:
        
             MyExtensions = (".txt", ".docx")
             MyFolder = "Documents"
             associate_folders_with_extensions(MyExtensions, MyFolder)
    """
    ArchivosParaEstaCarpeta = []
    
    for archivo in listdir(ruta):
        if archivo.endswith(extensiones_de_archivos) == True and archivo not in ArchivosExcepciones and isfile(ruta+archivo):
            """"
                "file not in FilesExceptions" checks that our file is not
                 in the list of FilesExceptions, if it is, this file will not
                 is added to the FilesForThisFolder list, since we don't want to move the
                 files contained in FilesExceptions.
                 isfile() checks that it is a file and a folder, because if there is a folder that
                 has an extension in its name, the program will generate an error.
            """
            ArchivosParaEstaCarpeta.append(ruta+archivo)
    """
         The endswith() method checks that the file ends with the desired extension.
         example:
        
            archivo = "Imagen.png"
            extencion = ".png"    
            x = archivo.endswith(extenxion)
            print(x)
            
         In this case, when the string "Image.png" ends with the extension ".png", x will be True.
        
         With this loop, the content of the current directory is listed using the function
         listdir() of the module os. Next, the list that returns and stores is traversed
         each value in file by iteration (repetition). with the if we check if the file
         ends with the desired extension, and only if so, is that file added to the documents list.
    """
    
    return ArchivosParaEstaCarpeta

if __name__ == "__main__":
    """
         This code will only be executed if this file has not been imported.
         That is, only if it has been executed using python Order.py.
         If it was imported through an import Order, this code will not be
         will execute
    """

    parse = ArgumentParser() # Make an instance of the ArgumentParser class
    
    # We create parameters for our script, if they are not used, we will use default data:
    parse.add_argument("-rf", "--directoryFile", help="se le indica la ruta donde se encuentran los archivos que queremos organizar.", type=str, default="C:\Users\casti\Videos")
    parse.add_argument("-ro", "--directoryOutput", help="Se le indica la ruta donde se creara las carpetas y se ordenara los elementos en ellas.", type=str, default="C:\Users\casti\Videos")

    # we pass the parameters of the program to be able to use them
    parse = parse.parse_args()
    # The default values are the path "C:\Users\casti\Videos", that is, the current directory.
    
    
    # Here we make an instance of the COLOR class to be able to use colors in our prints:
    _COLOR = COLOR()
    BannerAlerta = "{}[{}!{}] {}".format(_COLOR.LIGHTGREEN_EX, _COLOR.LIGHTMAGENTA_EX, _COLOR.LIGHTGREEN_EX, _COLOR.LIGHTWHITE_EX)
    BannerInformativo = "{}[{}*{}] {}".format(_COLOR.LIGHTGREEN_EX, _COLOR.LIGHTRED_EX, _COLOR.LIGHTGREEN_EX, _COLOR.LIGHTYELLOW_EX)
    BannerOtros = "{}[{}${}] {}".format(_COLOR.LIGHTGREEN_EX, _COLOR.LIGHTBLUE_EX, _COLOR.LIGHTGREEN_EX, _COLOR.LIGHTWHITE_EX)
    
    """
         In this list we put the special files that we do not want to move, as is the case
         of our script. __file__ stores the name of this script as a value, so
         If we change the name of this file, this variable will be in charge of putting its value
         correspondent
    """
    ArchivosExcepciones = [__file__.split("\\")[-1], "__TXT__"\"requirements.txt"]
    """
        __file__ = 'C:\\Users\\Usuario\\Documents\\GitHub\\Organizar-Archivos-Por-Su-Extension\\Orden.py'
    
        >>> archivo = __file__.split("\\")
        >>> print(archivo)
        ['C:', 'Users', 'Usuario', 'Documents', 'GitHub', 'Organizar-Archivos-Por-Su-Extension', 'Orden.py']
        >>> print(archivo[-1])
        "Orden.py"
        
    """


    carpetas = ["Documents", "Photos", "Videos", "Music", "Other"]
    create_folders_if_not_exist(carpetas, ruta="C:\Users\casti\Videos")
    # Create the necessary folders
    
    extensionesdocumentos = [   
                                (".aac", ".adt",".adts",".accdb",".accde",".accdr",".accdt",".docm",".dot",".dotx",".eml",".pdf",".mdb",".pot",".potm",".potx",".ppam",".pps",".ppsm",".ppsx",".psd",".pptm",".pst",".pub",".sldm",".sldx",".vsdm",".vsdx",".vss",".vssm",".vst",".vstm",".vstx", ".docx", ".wks", ".xla", ".xlam", ".xll", ".xlm", ".xls", ".xlsm", ".xlsx", ".xlt", ".xltm", ".xltx", ".txt", ".odt", ".xlsx", ".ppt", ".pptx"), # documents
                                (".png", ".jpg", ".jpeg", ".gif", ".tiff", ".bmp"),                 # Photos
                                (".mp4", ".mkv", ".avi", ".mov", ".flv", ".divx"),                  # Videos
                                (".mp3", ".aac", ".wav", ".aiff", ".wma", ".opus", ".ogg"),         # Music
                                (   
                                    ".py", ".rar", ".zip", ".html", ".tmp", ".dat", ".exe", ".deb", 
                                    ".dmg", ".psd", ".c", ".asm", ".java",".iso",".xml", ".rst"
                                ), # Other
                            ]
    
    for carpetaNumero in range(0, len(carpetas)):
        """
             With this loop, we associate the folders and extensions using an index.
             This loop will repeat as many times as there are folders in the list. and will keep
             int values in the variable folderNumber.
        """
        
        ListaDeArchivos = asociar_carpetas_con_extensiones(carpetaNumero, extensionesdocumentos[carpetaNumero], ruta="C:\Users\casti\Videos", ArchivosExcepciones=ArchivosExcepciones) 
        print("{} Files to save in the folder {}, in total an amount of {}:".format(BannerOtros, carpetas[carpetaNumero], len(ListaDeArchivos)))
        print("\n".join(ListaDeArchivos))
        """
            Here we print the files that are going to be saved in the folder.
        """
        
        
        for archivo in ListaDeArchivos:
            """
                 This loop moves the files from the desired directory to the folders created or already
                 existing ones that were specified.
            """
            try:
                print("{} Moving the file ({}) to folder ({})".format(BannerInformativo, archivo, carpetas[carpetaNumero]))
                move(archivo, parse.directoryOutput+carpetas[carpetaNumero])
            except Error:
                print("{} The file {} \t already exists in the directory {}".format(BannerAlerta, archivo, carpetas[carpetaNumero]))