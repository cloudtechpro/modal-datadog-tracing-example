import modal
from modal import Image
from ddtrace import tracer, patch_all

image_dd = (
    Image.debian_slim()
    .dockerfile_commands('RUN pip install --target /dd_tracer/python/ ddtrace')
    .dockerfile_commands('COPY --from=datadog/serverless-init:1 /datadog-init /app/datadog-init')
    .dockerfile_commands('ENV DD_SERVICE=example-get-started')
    .dockerfile_commands('ENV DD_ENV=demo')
    .dockerfile_commands('ENV DD_VERSION=1')
    .dockerfile_commands('ENV DD_TRACE_ENABLED=true')
    .dockerfile_commands('ENV DD_SITE=datadoghq.com')
    .dockerfile_commands('ENV DD_TRACE_PROPAGATION_STYLE=datadog')
    .dockerfile_commands('ENV DD_LOGS_INJECTION=true')
    .dockerfile_commands('RUN chmod a+x /app/datadog-init')
    .dockerfile_commands('ENTRYPOINT ["/app/datadog-init"]')
    
)

patch_all()

stub = modal.Stub(image=image_dd, name="get-started")

@stub.function(secrets=[modal.Secret.from_name("dd-api-key")])
def square(x):
    # Use the tracer to create a new span
    with tracer.trace("square", service="example-get-started"):
        print("This code is running on a remote worker!")
        return x**2

@stub.local_entrypoint()
def main():
    print("the square is", square.remote(42))