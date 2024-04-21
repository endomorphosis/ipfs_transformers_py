from setuptools import setup

setup(
	name='ipfs_transformers',
	version='0.0.1',
	packages=[
        'ipfs_transformers',
        'ipfs_transformers.model_manager'
        'ipfs_transformers.model_manager.ipfs_kit_lib',
        'ipfs_transformers.model_manager.orbitdb_kit_lib',
	],
	install_requires=[
        'ipfs_datasets@git+https://github.com/endomorphosis/ipfs_datasets.git',
        'orbitdb_kit@git+https://github.com/endomorphosis/orbitdb_kit.git',
        'ipfs_kit@git+https://github.com/endomorphosis/ipfs_kit.git',
        'transformers',
        'torch',
        'torchvision',
        'numpy',
        'torchtext',
		'urllib3',
		'requests',
		'boto3',
	]
)