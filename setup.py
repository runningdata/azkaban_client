from setuptools import setup

setup(name='azkaban_client',
      version='0.0.6',
      description='azkaban_client based on azkaban restful apis',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Text Processing :: Linguistic',
      ],
      long_description=open('README.md').read(),
      keywords='azkaban client',
      url='http://github.com/ruoyuchen/azkaban_client',
      author='ruoyuchen',
      author_email='smhsma@aliyun.com',
      license='MIT',
      packages=['azkaban_client'],
      install_requires=[
          'requests',
      ],
      include_package_data=True,
      zip_safe=False)
