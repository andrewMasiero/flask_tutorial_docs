from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    pakcages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
