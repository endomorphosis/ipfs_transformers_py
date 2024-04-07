import os
# TODO: Make template match updates from ipfs_transformers.py
class AutoDownloadModel():
	def __init__(self, collection=None, meta=None):
		if os.getuid() == 0:
			if meta is not None and type (meta) == dict:
				if "local_path" in meta:
					self.local_path = meta["local_path"]			
				else:
					self.local_path = "/huggingface/"
				if "ipfs_path" in meta:
					self.ipfs_path = meta["ipfs_path"]
				else:
					self.ipfs_path = "/ipfs/"
				if "s3_cfg" in meta:
					self.s3cfg = meta["s3_cfg"]
				else:
					self.s3cfg = None
				if "role" in meta:
					self.role = meta["role"]
				else:
					self.role = "leecher"
			else:
				self.local_path = "/huggingface/"
				self.ipfs_path = "/ipfs/"
				self.s3cfg = None
				self.role = "leecher"
				meta = {
					"local_path": self.local_path,
					"ipfs_path": self.ipfs_path,
					"s3_cfg": self.s3cfg,
					"role": self.role
				}
		else:
			if meta is not None and type (meta) == dict:
				if "local_path" in meta:
					self.local_path = meta["local_path"]
				else:
					self.local_path = os.path.join(os.getenv("HOME") , ".cache/huggingface/")
				if "ipfs_path" in meta:
					self.ipfs_path = meta["ipfs_path"]
				else:
					self.ipfs_path = os.path.join(os.getenv("HOME") , ".cache/ipfs/")
				if "s3_cfg" in meta:
					self.s3cfg = meta["s3_cfg"]
				else:
					self.s3cfg = None
				if "role" in meta:
					self.role = meta["role"]
				else:
					self.role = "leecher"
			else:
				self.local_path = os.path.join(os.getenv("HOME") , ".cache/huggingface/")
				self.ipfs_path = os.path.join(os.getenv("HOME") , ".cache/ipfs/")
				self.s3cfg = None
				self.role = "leecher"
				meta = {
					"local_path": self.local_path,
					"ipfs_path": self.ipfs_path,
					"s3_cfg": self.s3cfg,
					"role": self.role
				}
		from model_manager import model_manager as model_manager
		self.model_manager = model_manager(collection, meta)
		self.model_manager.load_collection_cache()
		self.model_manager.state()
				
	def download(self, **kwargs):
		# NOTE: Add kwarg for output directory where downloads are stored
		# if "local_path" in kwargs:
		# 	self.local_path = kwargs["local_path"]
		# if "ipfs_path" in kwargs:
		# 	self.ipfs_path = kwargs["ipfs_path"]
		
		model_name = None
		cid = None
		if "model_name" in kwargs:
			if "/" in kwargs["model_name"]:
				model_name = kwargs["model_name"].split("/")[1]
				pass
			elif "https://" in kwargs["model_name"]:
				model_name = kwargs["model_name"].split("/")[-1]
				pass
			else:
				model_name = kwargs["model_name"]
			pass
		elif "cid" in kwargs:
			cid = kwargs["cid"]
		if model_name != None:
			try:
				results = self.model_manager.download_model(model_name, **kwargs)
			except Exception as e:
				raise e
			finally:
				pass
			return os.path.join(self.local_path, model_name)
		else:
			try:
				results = self.model_manager.download_ipfs(cid, os.path.join(self.local_path, cid), **kwargs)
			except Exception as e:
				raise e
			finally:
				pass
			return os.path.join(self.local_path, cid)
		pass


class Huggingface_Template():
# START AUTO_DOWNLOAD
	@staticmethod
	def from_auto_download(model_name, **kwargs):
		from transformers import Huggingface_Template
		this_download = AutoDownloadModel()
		download_folder = this_download.download(model_name=model_name, **kwargs)
		return Huggingface_Template.from_pretrained(
			download_folder, 
			local_files_only=True,
			**kwargs
		)
# END AUTO_DOWNLOAD

# START FROM_IPFS
	@staticmethod
	def from_ipfs(cid, **kwargs):
		from transformers import Huggingface_Template
		this_download = AutoDownloadModel()
		download_folder = this_download.download(cid=cid, **kwargs)
		return Huggingface_Template.from_pretrained(
			download_folder, 
			local_files_only=True,
			**kwargs
		)
# END FROM_IPFS

if __name__ == "__main__":
	AutoModel.from_auto_download("google-bert/law-LLM-GGUF-Q4_0")
	print("done")