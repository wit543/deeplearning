# Deeplearning

## Setup

### Install from environment.yml

```bash
# /path/to/reository/
> conda env create -f environment.yml
```

activate anaconda environment

```bash
> activate deeplearning # window
> source activate deeplearning # linux/ mac
```

Download dataset

```bash
deeplearning> python
>>> from keras.datasets import mnist
>>> mnist.load_data()
>>> quit()
```

### Manual install

Create new anaconda environment

```bash
> conda create -n deeplearning python=3.6
```

activate anaconda environment

```bash
> activate deeplearning # window
> source activate deeplearning # linux/ mac
```

install the library 

```bash 
deeplearning> conda install -c conda-forge scipy tensorflow keras pillow matplotlib jupyter
```

Download dataset

```bash
deeplearning> python
>>> from keras.datasets import mnist
>>> mnist.load_data()
>>> quit()
```

## download image

Download image file
```
download file from http://158.108.138.156:5000/
```

import dockefile

```
> docker load < busybox.tar.gz
```


## run image

```bash
> docker run --rm -p 8888:8888 wit543/deeplearning:circleci  /bin/bash -c "source activate deeplearning && jupyter lab  --ip='0.0.0.0' --port=8888 --no-browser --allow-root"
```