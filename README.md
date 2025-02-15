![GitHub repo size](https://img.shields.io/github/repo-size/scottydocs/README-template.md)
![GitHub contributors](https://img.shields.io/github/contributors/scottydocs/README-template.md)
![GitHub stars](https://img.shields.io/github/stars/scottydocs/README-template.md?style=social)

# modal-datadog-tracing-example
Instrumenting Modal app with Datadog ddtrace

Instrumenting a Python function manually in a Modal app with ddtrace allows you to trace custom function executions and gather detailed performance insights, which can be invaluable for debugging and optimizing your application. This process involves initializing the Datadog tracer and then using it to trace specific blocks of code or functions within your Modal functions.

## Prerequisites

### Ensure ddtrace is Installed
Before you start, ensure that ddtrace is included in your project's dependencies. If you're managing dependencies via a requirements.txt file, add ddtrace to it and make sure it's included in your Modal app environment.

## Manual Instrumentation in Modal
Due to the nature of Modal's execution environment, direct use of command-line tools like ddtrace-run isn't applicable. Instead, you'll need to initialize and start the tracer manually within your code, then use the tracing API to instrument your functions.

In this example:

Configurations that set the global service name and environment for all traces. Adjust these settings according to your application's needs.

The typical flow for defining an image in Modal is [method chaining](https://jugad2.blogspot.com/2016/02/examples-of-method-chaining-in-python.html) starting from a base image, like this:

```
image = (
    Image.debian_slim(python_version="3.10")
    .apt_install("git")
    .pip_install("torch==2.2.1")
    .env({"HALT_AND_CATCH_FIRE": 0})
    .run_commands("git clone https://github.com/modal-labs/agi && echo 'ready to go!'")
)
```

In addition to being Pythonic and clean, this also matches the onion-like [layerwise](layerwise build process) build process of container images.

The patch(all=True) command is used to automatically instrument all supported libraries used within your app, enhancing the traces with more detailed information without manual intervention.

Inside instrumented_function, tracer.trace() is used to manually create a span that traces the execution of the function's logic. This is where you define what part of your function you want to trace, allowing Datadog to collect performance data for that specific code block.

## View Traces in Datadog
After deploying your instrumented Modal app and executing functions, you should see traces appearing in your Datadog APM dashboard. Ensure that your Datadog Agent is running and properly configured to receive traces from your application.

## Additional Notes
Remember to manage your API keys and application configuration securely, especially in production environments.

Manual instrumentation allows you to add custom tags and metrics to your traces, providing more detailed insights into the performance and behavior of your instrumented functions.

This example provides a foundation for manually instrumenting Python functions in a Modal app with ddtrace, enabling you to leverage Datadog's APM features for monitoring and optimizing your cloud functions.

## Contribution Guidelines
1. Fork the repository and create a new feature branch.
2. Follow best practice python coding and security standards.
3. Submit a pull request and request a review from a maintainer.

## Code of Conduct
All contributors must:
- Be respectful and inclusive.
- Avoid harassment or discriminatory behavior.
- Follow GitHub’s Community Guidelines.

## Governance Model
- The project is maintained by a core team of maintainers.
- Major decisions require consensus among maintainers.
- Security vulnerabilities are addressed privately before public disclosure.

