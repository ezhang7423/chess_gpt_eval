from setuptools import setup, find_packages

setup(
    name='chess_eval',
    version='1.0.0',
    url='https://github.com/ezhang7423/chess_gpt_eval.git',
    author='Adam karvonen and Eddie Zhang',
    author_email='adam.karvonen@gmail.com',
    description='chess bot evaluation',
    packages=['chess_eval'],    
    install_requires=["openai==0.28.0", "tiktoken==0.4.0", "tenacity==8.2.3", "python-chess==1.999", "matplotlib==3.8.0", "pandas==2.1.1"],
)
