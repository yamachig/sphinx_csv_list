from distutils.core import setup

setup(
    name='Sphinx csv-list',
    version='0.0.1',
    description='Sphinx extension to render CSV as HTML list',
    author='yamachi',
    license='MIT',
    packages=['sphinx_csv_list'],
    package_data={'sphinx_csv_list': ['**/*.html', '**/*.css']},
    install_requires=['Jinja2'],
)
