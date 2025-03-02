import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

__version__= "0.0.0"

REPO_NAME = 'Text-Summarization'
AUTH_USER_NAME = 'ravichandran1610'
SRC_REPO = 'textSummarizer'
AUTHOR_EMAIL = 'rravii.r@gmail.com'



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTH_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for NLP - Text Summarization app',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{AUTH_USER_NAME}/{REPO_NAME}',
    project_urls = {
        "Bug Tracker": f'https://github.com/{AUTH_USER_NAME}/{REPO_NAME}/issues'
    },
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src')
)