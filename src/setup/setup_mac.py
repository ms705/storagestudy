from setuptools import setup

setup(
   app=["src/main.py"],
   options={"py2app":
      {"argv_emulation": True, "includes": ["sip", "PyQt4"]}
   },
   setup_requires=["py2app"]) 

