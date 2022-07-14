from setuptools import setup

setup(
    name='etab',
    version='0.1.0',    
    description='ETAB: A Benchmark Suite for Visual Representation Learning in Echocardiography',
    url='https://github.com/ahmedmalaa/ETAB',
    author='Ahmed Alaa',
    author_email='amalaa@mit.edu',
    license='BSD 2-clause',
    packages=['etab'],
    install_requires=["numpy",
                      "pandas",
                      "torch",
                      "torchvision",                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Programming Language :: Python :: 3'
    ],
)