from setuptools import setup

package_name = 'operator_interface'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='Operator interface for sending commands',
    license='License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'operator_interface = operator_interface.operator_interface:main'
        ],
    },
)
