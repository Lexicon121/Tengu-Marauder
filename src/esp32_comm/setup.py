from setuptools import setup

package_name = 'esp32_comm'

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
    maintainer='Lexiecon',
    maintainer_email='your_email@example.com',
    description='Package for ESP32 communication node',
    license='License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'esp32_comm_node = esp32_comm.esp32_comm_node:main'
        ],
    },
)
