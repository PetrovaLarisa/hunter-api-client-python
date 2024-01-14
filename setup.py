from setuptools import setup, find_packages

setup(
  name='hunter_client',
  version='1.0.0',
  description='Python client for Hunter.io API',
  long_description=open('README.md').read(),
  url='https://github.com/PetrovaLarisa/hunter-api-client-python',
  author='Larysa Petrova',
  author_email='mamapanama1984@gmail.com',
  license='MIT',
  packages=find_packages(),
  install_requires=[
    'requests'
  ],
  keywords=['hunter.io', 'api client'],
  classifiers=[
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ]
)