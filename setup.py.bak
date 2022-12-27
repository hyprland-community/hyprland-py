from setuptools import setup, find_packages
with open('.gitignore', 'r') as f:
    exclude = f.read().splitlines()

print(find_packages(exclude=exclude))

setup(
    name='hyprland.py',
    version='0.1',
    license='MIT',
    author="flicko",
    author_email='flickerdroid211@gmail.com',
    description='An unofficial async python wrapper for Hyprland\'s IPC supposed to somewhat work like awesomewm api in lua',
    packages=find_packages('hyprland'),
    url='https://github.com/hyprland-community/hyprland-py',
    keywords='hyprland async ipc wrapper',
    install_requires=[],
)