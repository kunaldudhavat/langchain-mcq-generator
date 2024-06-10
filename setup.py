from setuptools import find_packages,setup

setup(
    name='mcq-generator',
    version='0.0.1',
    author='Kunal Dudhavat',
    author_email='kunal.dudhavat@gmail.com',
    install_requires=["openai","langchain_openai","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)