# Python Apache Spark

## To run:

- Locally using `python <filename>.py`
- Use `spark-submit` to run on a cluster:

```
$ spark-submit --master local[`nproc`] <filename>.py
$ spark-submit --master k8s://https://<k8s-apiserver-host>:<k8s-apiserver-port> --conf spark.executor.instances=1 --conf spark.kubernetes.container.image=spark:python3 --conf spark.kubernetes.file.upload.path=/tmp --deploy-mode cluster <filename>.py
```
