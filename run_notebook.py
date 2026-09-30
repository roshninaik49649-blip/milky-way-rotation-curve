import sys, nbformat
from nbclient import NotebookClient

nb_path, out_path = sys.argv[1], sys.argv[2]
nb = nbformat.read(nb_path, as_version=4)
client = NotebookClient(nb, timeout=7200, kernel_name='python3')
client.execute()
nbformat.write(nb, out_path)
print("NOTEBOOK EXECUTED OK ->", out_path)
