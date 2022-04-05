from setuptools import find_packages, setup

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Parker-X',
  version='0.0.1',
  description='A very basic Module',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Parker',
  author_email='harshrawat096@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='cal', 
  packages=find_packages(),
  install_requires=[''] 
)