from setuptools import setup
from setuptools import find_packages
from socialfeeder.utilities.constants import __VERSION__

setup(
     name='socialfeeder',
     version=__VERSION__,
     author='datnguye',
     author_email='datnguyen.it09@gmail.com',
     packages=find_packages(),
    include_package_data=True,
     url='https://github.com/datnguye',
     license='MIT',
     description='A package to feed things on social',
     long_description_content_type="text/markdown",
     long_description=open('README.md').read(),
     install_requires=[
       'selenium==3.141.0',
       'webdriver-manager==2.5.3',
       'beautifulsoup4==4.9.1',
       'lxml==4.6.1',
     ],
     python_requires='>=3.7.5',
     entry_points = {
        'console_scripts': [
            'feeder = socialfeeder.__main__:main'
        ],
    }
)