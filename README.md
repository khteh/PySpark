# Python Apache Spark

## To run:

(1) Locally using `python <filename>.py`

    ```
    $ pipenv run spark-submit --master local[`nproc`] <filename>.py
    ```

(2) Luanch in Cluster mode.

- Create the necessary RBAC resources:
  ```
  $ kubectl apply -f spark_rbac.yml
  ```
- Use `spark-submit` to run on a cluster:
  ```
  $ pipenv run spark-submit --master k8s://https://<k8s-apiserver-host>:<k8s-apiserver-port> --conf spark.executor.instances=1 --conf spark.kubernetes.container.image=spark:python3 --conf spark.kubernetes.file.upload.path=/tmp --conf spark.kubernetes.authenticate.driver.serviceAccountName=sa-apache-spark --deploy-mode cluster <filename>.py
  ```

`<k8s-apiserver-host>:<k8s-apiserver-port>` can be found from `kubectl cluster-info` output. However, this would not work with rbac without using authenticating proxy.

- Use the authenticating proxy, `kubectl proxy` to communicate to the Kubernetes API.

```
$ kubectl proxy
$ pipenv run spark-submit --master k8s://http://127.0.0.1:8001 --conf spark.executor.instances=1 --conf spark.kubernetes.container.image=spark:python3 --conf spark.kubernetes.file.upload.path=/tmp --conf spark.kubernetes.authenticate.driver.serviceAccountName=sa-apache-spark --deploy-mode cluster --name TextFile <path to>TextFile.py
```

TODO: Create `Dockerfile` and build a docker image
