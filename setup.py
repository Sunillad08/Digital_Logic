  
from setuptools import setup
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='LogicPy',
  version='0.0.1',
  description='Implementation of logic circuits using python',
  long_description=open('README.md').read(),
  url='https://github.com/Sunillad08/Digital_Logic',  
  author='Sunil Lad & Parth Khanolkar',
  author_email = 'ladsunil08@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Logic circuit , pylogic', 
  packages=['LogicPy'],
  install_requires=[''] 
)