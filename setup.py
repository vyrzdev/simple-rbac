from setuptools import setup

with open('README.rst') as readme:
    next(readme)
    long_description = ''.join(readme).strip()

setup(
    name='SimpleAccessControl',
    version='0.1.1',
    description='A simple role based access control utility - forked from simple-rbac by tonyseek on GitHub',
    long_description=long_description,
    keywords='rbac permission acl access-control permissions-system',
    author='Benjamin Parsons-Willis',
    author_email='ben@vyrz.dev',
    url='https://github.com/vyrzdev/simple-rbac',
    license='MIT License',
    packages=['rbac'],
    zip_safe=False,
    platforms=['Any'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
