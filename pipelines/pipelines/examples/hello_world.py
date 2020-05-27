from dagster import pipeline, solid, execute_pipeline, ScheduleDefinition


@solid
def get_name(context) -> str:
    return 'dagster'


@solid
def hello(context, name: str) -> str:
    context.log.info('Hello, {name}!'.format(name=name))
    return name


@pipeline
def hello_pipeline():
    hello(get_name())


"""Define schedule for this pipeline"""
schedule = ScheduleDefinition(
    name='hello_pipeline_schedule',
    cron_schedule='* * * * *',
    pipeline_name='hello_pipeline',
    environment_dict={'storage': {'filesystem': {}}},
)


if __name__ == '__main__':
    result = execute_pipeline(hello_pipeline)
    assert result.success
    name = result.result_for_solid('hello').output_value()
    print(name)
