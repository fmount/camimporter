BUILD="build"
DIST="dist"
PRE="requirements.txt"
PKG_NAME_EGG="camimporter.egg-info"
AUTHORS="AUTHORS"
CLOG="ChangeLog"


clean:
	@echo Removing build directories
	rm -rf $(BUILD) $(DIST) $(PKG_NAME_EGG)
	@echo Removed misc files
	rm $(AUTHORS) $(CLOG)


pre:
	@echo Installing prerequisites using pip
	 pip install -r $(PRE) --upgrade

build:
	@echo Building the camimporter package
	python setup.py sdist


install:
	@echo Installing the camimporter package on the system
	python setup.py install


buildlocal: pre
	@echo Building local dist package on the specified dir
	python setup.py install --root=$(BUILD)


.PHONY: install
