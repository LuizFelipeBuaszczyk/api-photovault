FROM quay.io/minio/aistor/minio:latest

# Criar diretórios necessários
RUN mkdir -p /mnt/data \
    && mkdir -p /etc/minio/certs

COPY minio.license /minio.license

EXPOSE 9000
EXPOSE 9001

CMD ["minio", "server", "/mnt/data", "--license", "/minio.license"]
