from setuptools import setup

setup(
    name='envkey_action',
    version='0.1',
    packages=['envkey_action'],
    install_requires=[
        'envkey',
    ],
    entry_points='''
        [console_scripts]
        envkey-action=envkey_action:export_env
    ''',
)