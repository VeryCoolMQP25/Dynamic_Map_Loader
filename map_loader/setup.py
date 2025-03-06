from setuptools import setup

package_name = 'map_loader'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools', 'rclpy', 'nav2_msgs'],
    zip_safe=True,
    author='Your Name',
    author_email='your_email@example.com',
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='Map loading node for ROS 2',
    license='TODO',
    entry_points={
        'console_scripts': [
            'map_loader = map_loader.map_loader:main'
        ],
    },
)
