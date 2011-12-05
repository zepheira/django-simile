from setuptools import setup, find_packages

setup(
    name = "django-simile",
    version = "2.2.0a1",
    description = "A rebundling of some of the Simile widgets for use by Django apps",
    url = "http://www.simile-widgets.org/",
    packages = find_packages(),
    include_package_data=True,
    install_requires=('django', 'django-compressor')
)
