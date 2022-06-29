from setuptools import setup

setup(
    name = 'secal',
    version='0.0.1',
    description='Section Analysis - modelling and analysis of custom cross-sections',
    author = 'Maurício Bonatte',
    author_email='mbonatte@ymail.com',
    url = 'https://github.com/mbonatte/SectionAnalysis',
    license='MIT',
    long_description=open('README.md').read(),
    
    # Dependencies
    install_requires=['numpy', 'matplotlib'],
    
    # Packaging
    packages =[ 'secal'],
    
)