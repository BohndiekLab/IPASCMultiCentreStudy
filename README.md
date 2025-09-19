# Code for "International multi-centre performance evaluation of copolymer-in-oil tissue-mimicking material for acoustic and optical imaging applications." 

**Code and data by: Lina Hacker and Thomas Else. Several others contributed to phantom development. Please see the paper for details.**

This is the code used to generate the multispectral optoacoustic tomography (MSOT) figures presented in the paper "International multi-centre performance evaluation of copolymer-in-oil tissue-mimicking material for acoustic and optical imaging applications. 

## Accessing the data

Data will be uploaded to an online repository when the paper is published.

## Setting up the code environment.

This code can be downloaded using a link on the GitHub website, or using the following command: 

```{bash}
git clone https://github.com/BohndiekLab/IPASCMultiCentreStudy
```

To run the code, make sure you have a suitable Python environment set up on your computer. We recommend using a tool like [https://www.anaconda.com/](Anaconda), [https://docs.python.org/3/library/venv.html](virtual environments), or [https://github.com/astral-sh/uv](uv) to manage different Python versions. This analysis was run using Python 3.12.3, with versions of each Python library (e.g. NumPy, patato, etc.) specified in the `uv.lock` and `requirements.txt` files. 


### Option 1: Installing via uv:

If using [https://github.com/astral-sh/uv](uv) to manage the Python version, you can simply run the following command to restore the Python version.

```{bash}
cd IPASCMultiCentreStudy
uv sync
```

### Option 2: Installing via virtual environments and pip:

Alternatively, you can recreate the Python environment using pip (and ideally use a virtual environment too). For guidance on setting up a virtual environment see [https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/](here). Once you have set up a virtual environment run the following:

```{bash}
cd IPASCMultiCentreStudy
pip install -r requirements.txt
```

### Option 3: Anaconda:

First, I would recommend creating a new Anaconda environment, and then activate it as usual. Once you have done so, you can run the following commands:

```{bash}
cd IPASCMultiCentreStudy
pip install -r requirements.txt
```

## Running the code.

To run the code, I would recommend using Jupyter lab. This will be installed automatically if you follow the guidance above. 

```{bash}
jupyter-lab 
```

This will open an interface, from which you can run `apply_analysis.ipynb` and `image_registration.ipynb`. 


