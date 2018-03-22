FROM continuumio/miniconda3:latest
WORKDIR /workspace

RUN conda update -n base conda

COPY environment.yml ./

RUN conda env create environment.yml

COPY . .

EXPOSE 8888

# CMD [ "source activate deeplearning && jupyter lab" ]

# docker run --rm -p 54355:8888 wit543/deeplearning:latest  /bin/bash -c "source activate deeplearning && jupyter lab  --ip='0.0.0.0' --port=8888 --no-browser --allow-root"
