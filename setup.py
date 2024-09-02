from setuptools import setup

setup(
	name='ipfs_transformers_py',
	version='0.0.3',
	packages=[
        'ipfs_transformers_py',
	],
	install_requires=[
                'orbitdb_kit_py',
                'ipfs_kit_py',
                'ipfs_model_manager_py',
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
