from setuptools import setup, find_packages

from articles import get_version
import setuplib

packages, package_data = setuplib.find_packages('articles')

setup(
    name = "feincms-articles",
    packages = packages,
    package_data=package_data,
    include_package_data=True,
    install_requires=[
        "FeinCMS",
        "django-mptt",
        "django-pagination",
    ],
    version = get_version(),
    description = "Provides Articles using (FeinCMS content) with categories and tags.",
    author = "Incuna Ltd",
    author_email = "admin@incuna.com",
    url = "https://github.com/incuna/feincms-articles/",
)
