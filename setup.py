from setuptools import setup

setup(name="systeminfo",
            version="0.1",
            description="Basic system information for COMP30670",
            url="",
            author="Manjunath Sanjiv Kulkarni",
            author_email="manjunath.kulkarni@ucdconnect.ie",
            license="GPL3",
            packages=['systeminfo1'],
            entry_points={
                'console_scipts':['comp30670_systeminfo1=systeminfo1.main:main']})