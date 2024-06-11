from setuptools import setup

setup(
	name='ipfs_transformers',
	version='0.0.1',
	packages=[
        'ipfs_transformers',
	],
	install_requires=[
        # 'ipfs_datasets@git+https://github.com/endomorphosis/ipfs_datasets.git',
        'orbitdb_kit@git+https://github.com/endomorphosis/orbitdb_kit.git',
        'ipfs_kit@git+https://github.com/endomorphosis/ipfs_kit.git',
        'ipfs_model_manager@git+https://github.com/endomorphosis/ipfs_model_manager.git',
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
