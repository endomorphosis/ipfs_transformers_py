import os
import inspect 
import transformers

init_header = """
from .ipfs_kit import ipfs_kit
from .s3_kit import s3_kit
from .test_fio import test_fio
"""

init_output = init_header

input_file = "ipfs_transformers_template.py"
output_file = "ipfs_transformers.py"
init_file = "__init__.py"
classes = []


for name, obj in inspect.getmembers(transformers):
	if inspect.isclass(obj):
		try:
			if hasattr(obj, "from_pretrained") and callable(getattr(obj, "from_pretrained")):
				cleaned_class = str(obj).split(".")[-1].strip("'>")
				classes.append(cleaned_class)
		except Exception as e:
			continue


with open(f"{os.path.dirname(__file__)}/{input_file}", "r") as f:
    ipfs_huggingface = f.read()


# Finds index of class Huggingface_Template() everything before this index is header
header = ipfs_huggingface[0 : ipfs_huggingface.find("class Huggingface_Template():")]

# Added these comments for easy identification of the start and end of the auto download template 
auto_download_template = ipfs_huggingface[ipfs_huggingface.find("# START AUTO_DOWNLOAD") : ipfs_huggingface.find("# END AUTO_DOWNLOAD")]
from_ipfs_template = ipfs_huggingface[ipfs_huggingface.find("# START FROM_IPFS") : ipfs_huggingface.find("# END FROM_IPFS")]

# Clean up step to remove the comments
auto_download_template = auto_download_template.replace("# START AUTO_DOWNLOAD", "").replace("# END AUTO_DOWNLOAD", "")
from_ipfs_template = from_ipfs_template.replace("# START FROM_IPFS", "").replace("# END FROM_IPFS", "")



with open(f"{os.path.dirname(__file__)}/{output_file}", "w") as f:
	f.write(header)


for transformer_class in classes:
	class_specific_auto_download = auto_download_template.replace("Huggingface_Template", transformer_class)
	class_specific_from_ipfs = from_ipfs_template.replace("Huggingface_Template", transformer_class)

	init_specific_output = f"from .ipfs_transformers import {transformer_class}\n"
	init_output += init_specific_output

	# This looks a little messy but it's just to make the output file look nice
	output = f"""
class {transformer_class}(): {class_specific_auto_download} 
{class_specific_from_ipfs}

"""

	with open(f"{os.path.dirname(__file__)}/{output_file}", "a") as f:
		f.write(output)

	write_init_file = f"{os.path.dirname(__file__)}/{init_file}"
	with open(f"{os.path.dirname(__file__)}/{init_file}", "w") as f:
		f.write(init_output)

print("Done!")