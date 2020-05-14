#encoding:utf-8
import glob,os,re,sys,tarfile

path ="lib"
all_file = glob.glob(os.path.join(path,'*.py'))

ext_outside = """extensions = [
{}
]"""

Ext_inside='''  Extension(
        "{}",["{}"]
    ),    
'''

list_ext = ""

tar_list =['db.py','template/','logs/','etc','tmp']

for files in all_file:
    files_new = files.split(".")[0].replace("/",".")
    Ext_name = Ext_inside.format(files_new,files)
    list_ext = "".join(list_ext + Ext_name)
    tar_file = "".join(files.split(".")[0] + ".so")
    tar_list.append(tar_file)

ext_outside_all = ext_outside.format(list_ext)
setup_py ="""
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
{}
setup(
    name = "lib"
    ext_modules = cythonize(extensions),
)
""".format(ext_outside_all)

with open("setup.py","w") as f:
    f.write(setup_py)

os.system("python setup.py build_ext --inplace")
os.system("rm -rf logs/*")

tar_files = tarfile.open("".join("get_sql" + ".gz"),"w:gz")
for files in tar_list:
    tar_files.add(files)
tar_files.close()
