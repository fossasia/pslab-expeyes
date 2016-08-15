DESTDIR =
SOURCES = $(shell find .. -name "*.py")
POFILES = $(shell ls *.po)
MOFILES = $(patsubst %.po, %.mo, $(POFILES))
LANG = $(patsubst %.po, %, $(POFILES))

all: $(MOFILES)

%.mo: %.po
	msgfmt --output-file=$@ $<

$(POFILES): messages.pot
	for f in $(POFILES); do \
	  msgmerge --update --previous $$f messages.pot; \
	done

messages.pot: $(SOURCES)
	if [ -f $@ ]; then \
	  xgettext --output=$@  --language=python --join-existing --keyword=_ --add-location $(SOURCES); \
	else \
	  xgettext --output=$@  --language=python --keyword=_ --add-location $(SOURCES); \
	fi

clean:
	rm -f messages.pot *.mo *~

install: all
	for l in $(LANG); do \
	  install -d $(DESTDIR)/usr/share/locale/$$l/LC_MESSAGES; \
	  install -m 644 $$l.mo $(DESTDIR)/usr/share/locale/$$l/LC_MESSAGES/expeyes.mo; \
	done

.PHONY: all clean install
