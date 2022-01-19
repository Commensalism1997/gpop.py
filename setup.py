from distutils.core import setup
setup(
  name = 'gpop.py',
  packages = ['gpop.py'],
  version = '0.1',
  license='MIT',
  description = 'Module that will help you collect data from gpop.io',
  author = 'Commensalism',
  author_email = 'kirill.lavlinskijb@gmail.com',
  url = 'https://github.com/Commensalism1997/gpop.py',
  download_url = 'https://github.com/Commensalism1997/gpop.py/archive/refs/tags/v_01.tar.gz',
  keywords = ['GPOP', 'ONLINE', 'GAME'],
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
