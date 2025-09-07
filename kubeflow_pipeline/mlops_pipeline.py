import kfp
from kfp import dsl

# Components of pipeline (container-based)
@dsl.container_component
def data_processing_op() -> dsl.ContainerSpec:
    return dsl.ContainerSpec(
        image="joevisco/my-mlops-app",
        command=["python", "src/data_processing.py"],
    )

@dsl.container_component
def model_training_op() -> dsl.ContainerSpec:
    return dsl.ContainerSpec(
        image="joevisco/my-mlops-app",
        command=["python", "src/model_training.py"],
    )

# Pipeline
@dsl.pipeline(
    name="MLOPS Pipeline",
    description="This is my first ever Kubeflow pipeline"
)
def mlops_pipeline():
    dp = data_processing_op()
    mt = model_training_op().after(dp)

# Compile to YAML (upload this in the KFP UI)
if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        pipeline_func=mlops_pipeline,
        package_path="mlops_pipeline.yaml",
    )
