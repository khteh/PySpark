# Python Apache Spark

## To run:

- Locally using `python <filename>.py`
- Use `spark-submit` to run on a cluster:

```
$ spark-submit --master local[`nproc`] <filename>.py
$ spark-submit --master k8s://https://<k8s-apiserver-host>:<k8s-apiserver-port> --conf spark.executor.instances=1 --conf spark.kubernetes.container.image=spark:python3 --conf spark.kubernetes.file.upload.path=/tmp --conf spark.kubernetes.authenticate.driver.serviceAccountName=sa-apache-spark --deploy-mode cluster <filename>.py
```

`<k8s-apiserver-host>:<k8s-apiserver-port>` can be found from `kubectl cluster-info` output
