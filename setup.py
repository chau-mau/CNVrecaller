from setuptools import setup, find_packages

setup(
    name='CNVrecaller',
    version='0.1',
    packages=find_packages(),  # Automatically discover packages
    scripts=['src/main.py'],  # Path to your script
    install_requires=[],  # Add any dependencies here
    description='A tool to convert CNVR genotypes in VCF files to binary or tertiary coding for downstream analyses based on presence and absence of CNVRs.',
    author='Dr. Nidhi Sukhija and Dr. Kanaka K. K.',
    author_email='nidhisukhija5@gmail.com',
    entry_points={
        'console_scripts': [
            'cnvrecaller=main:main',  # Replace 'main' with your module name if needed
        ],
    },
)
