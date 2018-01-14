import setuptools
from djsetup.version import Version


setuptools.setup(name='djsetup',
                 version=Version('0.0.1').number,
                 description='Django Setup Utility',
                 long_description=open('README.md').read().strip(),
                 author='Zack Kollar',
                 author_email='zackkollar@gmail.com',
                 url='http://path-to-my-packagename',
                 py_modules=['djsetup'],
                 install_requires=[
                     'virtualenv',
                     'django',
                     'django_extensions'
                 ],
                 license='MIT License',
                 zip_safe=False,
                 keywords='django boilerplate setup',
                 classifiers=['Packages', 'Boilerplate'])
