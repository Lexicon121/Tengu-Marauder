from setuptools import setup

package_name = 'motor_control'

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
    description='Package for motor control node',
    license='License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motor_control_node = motor_control.motor_control_node:main'
        ],
    },
)
