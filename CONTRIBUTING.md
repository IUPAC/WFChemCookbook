# Contributing

We welcome all community contributions to this work, whether it be a minor typo correction or a complex demonstration notebook.  There are a variety of ways you can help improve this resource, including:

## Issues

If you spot something wrong or missing, please let us know through an [issue](https://github.com/IUPAC/WFChemCookbook/issues).  No coding required.  Just drop a line so we can follow up and make sure the resource is even better for the next person who comes along.

## Pull Requests

More advanced practitioners should consider putting together a [pull request](https://github.com/IUPAC/WFChemCookbook/pulls).  Direct contributions are the fastest way to improve this work, whether it be because there's a quick editorial improvement or because we're missing the latest, greatest library.

## Installation

This project can be downloaded directly from the repository website or via

```sh .noeval
git clone git@github.com:IUPAC/WFChemCookbook.git
```

Install [pixi](https://pixi.prefix.dev/dev/installation/) and install the dependencies via pixi.

```sh .noeval
pixi install
```

To explore the cookbook locally run:

```sh .noeval
pixi run serve
```

### Further pixi tasks

Add a module:

```sh .noeval
pixi add <module name>
```

or

```sh .noeval
pixi add --pypi <module name>
```

Install packages

```sh .noeval
pixi run install
```

Clean cached packages

```sh .noeval
pixi run clean
```

Build the website (without serving) and check for broken links

```sh .noeval
pixi run build
```

If nothing works it is sometimes helpful to delete the `pixi.lock` file and clean the `.pixi` folder

The cache of the jupyter book build can be cleared (deletes `book/_build` folder)

TODO:: The build option "should" execute the notebooks and raise errors. This does not seem to work properly.
In addition the validity of links is checked.

```sh .noeval
pixi run execute
```
