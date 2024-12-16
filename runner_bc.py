import os
import shutil
import time

ES_path = "D:\\SW testing\\pyke3-1.1.1\\pyke-1.1.1\\my_projects\\firstAid"
# Path to the folder you want to delete
folder_path = ES_path+"\\compiled_krb"

# Check if the folder exists before attempting to delete it
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    # Use shutil.rmtree to delete the folder and all of its contents
    shutil.rmtree(folder_path)
    print(f"Deleted the folder: {folder_path}")
else:
    print(f"Folder not found: {folder_path}")
    

# ----------------------------------------------------------------------

import sys
#sys.path.append('D:\\SW testing\\pyke3-1.1.1\\pyke-1.1.1\\examples\\family_relations')
sys.path.append(ES_path)
import driver



#driver.fc_test()

#driver.bc_test()

driver.bc_test_two()


