# NEON AI (TM) SOFTWARE, Software Development Kit & Application Development System
#
# Copyright 2008-2025 Neongecko.com Inc. | All Rights Reserved
#
# Notice of License - Duplicating this Notice of License near the start of any file containing
# a derivative of this software is a condition of license for this software.
# Friendly Licensing:
# No charge, open source royalty free use of the Neon AI software source and object is offered for
# educational users, noncommercial enthusiasts, Public Benefit Corporations (and LLCs) and
# Social Purpose Corporations (and LLCs). Developers can contact developers@neon.ai
# For commercial licensing, distribution of derivative works or redistribution please contact licenses@neon.ai
# Distributed on an "AS IS” basis without warranties or conditions of any kind, either express or implied.
# Trademarks of Neongecko: Neon AI(TM), Neon Assist (TM), Neon Communicator(TM), Klat(TM)
# Authors: Guy Daniels, Daniel McKnight, Regina Bloomstine, Elon Gasper, Richard Leeds
#
# Specialized conversational reconveyance options from Conversation Processing Intelligence Corp.
# US Patents 2008-2021: US7424516, US20140161250, US20140177813, US8638908, US8068604, US8553852, US10530923, US10530924
# China Patent: CN102017585  -  Europe Patent: EU2156652  -  Patents Pending

from setuptools import setup, find_packages
from os import getenv, path


BASE_PATH = path.abspath(path.dirname(__file__))


def get_requirements(requirements_filename: str):
    requirements_file = path.join(BASE_PATH, "requirements", requirements_filename)
    with open(requirements_file, 'r', encoding='utf-8') as r:
        requirements = r.readlines()
    requirements = [r.strip() for r in requirements if r.strip() and not r.strip().startswith("#")]

    for i in range(0, len(requirements)):
        r = requirements[i]
        if "@" in r:
            parts = [p.lower() if p.strip().startswith("git+http") else p for p in r.split('@')]
            r = "@".join(parts)
            if getenv("GITHUB_TOKEN"):
                if "github.com" in r:
                    r = r.replace("github.com", f"{getenv('GITHUB_TOKEN')}@github.com")
            requirements[i] = r
    return requirements


PLUGIN_ENTRY_POINT = 'neon-stt-plugin-nemo = neon_stt_plugin_nemo:NemoSTT'


with open(path.join(BASE_PATH, "README.md"), "r") as f:
    long_description = f.read()


with open(path.join(BASE_PATH, "version.py"), "r", encoding="utf-8") as v:
    for line in v.readlines():
        if line.startswith("__version__"):
            if '"' in line:
                version = line.split('"')[1]
            else:
                version = line.split("'")[1]

setup(
    name='neon-stt-plugin-nemo',
    version=version,
    description='Nemo STT plugin for Neon',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/NeonGeckoCom/neon-stt-plugin-nemo',
    author='Neongecko',
    author_email='developers@neon.ai',
    license='BSD-3.0',
    packages=find_packages(),
    package_data={"neon_stt_plugin_nemo": ["*.yml"]},
    install_requires=get_requirements("requirements.txt"),
    extras_require={"docker": get_requirements("docker.txt")},
    zip_safe=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='mycroft plugin stt',
    entry_points={'mycroft.plugin.stt': PLUGIN_ENTRY_POINT}
)
