from setuptools import setup

setup(
	name='ipfs_transformers',
	version='0.0.1',
	packages=[
        'ipfs_transformers',
	],
	install_requires=[
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
