FROM alpine/git as git

ARG TEPLATE_URL=https://github.com/Bio-Tvorogok/react_template.git

RUN echo ${TEPLATE_URL}
RUN mkdir /template && git clone ${TEPLATE_URL} /template

FROM node:20-alpine as web_builder

WORKDIR /tmp/build
COPY --from=git /template .

RUN yarn install --production && yarn build

FROM python:3.11-slim as builder

ENV PYTHONFAULTHANDLER=1 \
    PYTHONBUFFERED=1 \
    PIP_NO_CACHE_DIR=OFF \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PYTHONPATH=/opt/app \
    PDM_VERSION=2.9.*

WORKDIR /opt/app

RUN pip install -U "pdm==$PDM_VERSION" "pip==23.2.1" && \
    pdm config venv.in_project false && \
    pdm config check_update false && \
    pdm config python.use_venv false && \
    apt update && apt install -y tar && \
    apt clean autoclean && \
    apt autoremove --yes && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

COPY pyproject.toml pdm.lock README.md /opt/app/
COPY --from=web_builder /tmp/build/build /tmp/build

RUN mkdir __pypackages__ && pdm install -v --prod --no-lock --no-editable && \
    tar -czvf template.tar.gz /tmp/build

FROM python:3.11-slim as runner

ENV PYTHONPATH=/opt/app/pkgs
COPY --from=builder /opt/app/__pypackages__/3.11/lib /opt/app/pkgs
COPY --from=builder /opt/app/template.tar.gz /opt/app/.

WORKDIR /opt/app
COPY . .

CMD ["python", "-m", "react_converter"]