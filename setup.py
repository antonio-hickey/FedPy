from setuptools import find_packages, setup

classifiers = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
]

setup(
 name='FedPy',
 version='1.1.6',
 description='Fetch official Federal Reserve data for your desired use.',
 lang_descrip=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
 url='https://github.com/antonio-hickey/FedPy',
 author='Antonio Hickey',
 author_email="antoniohickey99@gmail.com",
 license='MIT',
 classifiers=classifiers,
 keywords=['Federal Reserve', 'Economics', 'Finance'],
 packages=find_packages(),
 install_requires=[
         'wheel',
         'beautifulsoup4',
         'lxml',
         'pandas',
         'datetime',
         'requests',
     ],
)
