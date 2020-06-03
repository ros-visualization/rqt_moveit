#!/usr/bin/env python

from setuptools import setup

package_name = 'rqt_moveit'
version = '1.0.1'

setup(
    name=package_name,
    version=version,
    packages=[package_name],
    package_dir={'': 'src'},
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['plugin.xml']),
        ('share/' + package_name + '/resource',
            ['resource/moveit_top.ui']),
        ('lib/' + package_name, ['scripts/rqt_moveit'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author="Isaac Saito",
    maintainer="Isaac Saito, Arne Hitzmann",
    maintainer_email="iisaito@kinugarage.com, arne.hitzmann@gmail.com",
    keywords=["ROS 2"],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'An rqt-based tool that assists monitoring tasks for MoveIt2 motion planner developers and users.'
    ),
    license='BSD',
    scripts=['scripts/rqt_moveit'],
)
