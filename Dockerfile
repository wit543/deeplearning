FROM continuumio/anaconda3:latest
WORKDIR /workspace

RUN conda update -n base conda

COPY environment.yml ./

RUN conda env create environment.yml

COPY . .


CMD [ "source","activate","deeplearning","&&","jupyter", "lab" ]
