DESTDIR=/usr
BINDIR=${DESTDIR}/bin
ui:
	pyuic5 -x poleseeker_mainwindow.ui -o poleseeker_mainwindow.py

run: ui
	chmod a+x poleseeker.py
	./poleseeker.py

install: ui
	mkdir -p ${DESTDIR}/share/poleseeker
	cp -rf  *.py ${DESTDIR}/share/poleseeker/
	cp -rf poleseeker ${BINDIR}
	chmod a+x ${BINDIR}/poleseeker ${DESTDIR}/share/poleseeker/poleseeker.py