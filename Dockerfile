FROM continuumio/miniconda3:latest
WORKDIR /workspace

RUN conda update -n base conda

COPY environment.yml ./

RUN conda env create environment.yml

COPY . .
RUN bash -c "source activate deeplearning && python -c 'from keras.datasets import mnist; mnist.load_data()'"
# CMD [ "source activate deeplearning && jupyter lab" ]"
