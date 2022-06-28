# Galileo Experiments Extensions

This repository contains examples and ready-to-use implementations of Galileo clients for different service to easily start
an experiment.

The project mainly depends on the [galileo-experiments](https://github.com/edgerun/galileo-experiments) repository
and should help newcomers to understand the project with ready to go examples!

# Instructions

For now all documentation (i.e., infrastructure setup, configurations) can be found in the [main project](https://github.com/edgerun/galileo-experiments).

# Run notebooks

Notebooks are located in `notebooks`.
You need to install `galileo-experiments` in editable state to run the notebooks.
Inside `notebooks` import modules from `galileoexperiments`.

To install the project (assuming you already created and activated a virtual environment via `make venv`):

      pip install -e .
      ./bin/start-notebook.sh


The notebook requires multiple environment variables to fetch data from the data storages.
Therefore, the start script exports those (located in `bin/.env`) and starts the notebook server.
Checkout the [main repository](https://github.com/edgerun/galileo-experiments) for a detailed description of those.
