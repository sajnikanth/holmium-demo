Introduction
============

This is a demo for selenium and [holmium](http://holmiumcore.readthedocs.org)

Pre-Requisites
==============
* firefox
* On OSX

        sudo easy_install nose && \
        sudo easy_install pip && \
        sudo pip install -U selenium && \
        sudo pip install -U holmium.core
* On Ubuntu

        sudo apt-get install python-pip -y && \
        sudo pip install -U selenium && \
        sudo pip install -U holmium.core && \
        sudo pip install nose

Run
===
`nosetests test_vistaprint.py -v --with-holmium --holmium-browser=firefox`
