"""This modules registers dagster pipelines and their schedules"""
import sys

from dagster import RepositoryDefinition
from dagster.utils import script_relative_path

sys.path.append(script_relative_path('.'))

"""Import the pipeline module `HERE`"""
from pipelines.examples import hello_world


""" REGISTER PIPELINES HERE """
# Note that we can pass a function, rather than pipeline instance.
# This allows us to construct pipelines lazily, if, e.g.,
# initializing a pipeline involves any heavy compute
PIPELINES = {
    'hello_pipeline': lambda: hello_world.hello_pipeline,
}


""" register all the pipeline schedules in this list"""
SCHEDULES = [
    hello_world.schedule,
]


def define_repo():
    """Register pipelines with dagster. We register them by adding entry in
    to the pipeline_dict below.

    The key must be same name as pipeline funtion.

    The value must be a `lambda: pipeline_func` to load the pipelines lazyly
    """
    return RepositoryDefinition(
        name='dagster_pipelines',
        pipeline_dict=PIPELINES,
        schedule_defs=SCHEDULES
    )
