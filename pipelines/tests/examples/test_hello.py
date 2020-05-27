from dagster import execute_solid, execute_pipeline

from pipelines.examples.hello_world import hello, hello_pipeline


def test_hello_solid():
    res = execute_solid(hello, input_values={'name': 'anderson'})
    assert res.success
    assert res.output_value() == 'anderson'


def test_hello_pipeline():
    res = execute_pipeline(hello_pipeline)
    assert res.success
    name = res.result_for_solid('hello').output_value()
    assert name == 'dagster'
