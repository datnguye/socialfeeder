from setuptools import setup, find_packages

setup(
     name='socialfeeder',
     version='1.0.0',
     author='datnguye',
     author_email='datnguyen.it09@gmail.com',
     packages=find_packages(),
     url='https://github.com/datnguye/socialfeeder',
     license='MIT',
     description='A package to feed things on social',
     long_description_content_type="text/markdown",
     long_description=open('README.md').read(),
     install_requires=[
         
     ],
     python_requires='>=3.7.5',
     entry_points = {
        'console_scripts': [
            'feeder = socialfeeder.__main__:main'
        ],
    }
)