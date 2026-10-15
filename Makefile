#
# Use this Makefile with GNU make.
#
#
TOP ?= main.pdf

TOP_NAME = $(patsubst %.pdf,%,$(TOP))
EXT = pdf log aux out bbl blg toc snm nav fdb_latexmk fls bcf run.xml thm

STYS = $(wildcard texinputs/*.sty)

SUBDIRS ?= $(wildcard */.)

export TEXINPUTS := ./texinputs/:$(TEXINPUTS)

.PHONY: all clean $(SUBDIRS)

all: $(TOP)

%.pdf:%.tex $(STYS)
	@echo "LaTeX search path $(TEXINPUTS)"
	@latexmk -pdf $<

clean:
	@echo Cleaning $(TOP) and auxiliary files...
	@$(foreach file,$(TOP_NAME) $(TOP_NAME)-slide2 preview texput,$(foreach ext,$(EXT),[ -e $(file).$(ext) ] && rm -f $(file).$(ext) || true;))

full: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@
