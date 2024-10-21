"parameters": {
        "inputFilePattern": "gs://bkt-landing-zone-gcp/user.csv",
        "JSONPath": "gs://bkt-df-metadata-gcp/bq.json",
        "outputTable": "learning-gcp-cyb:user_data.users",
        "bigQueryLoadingTemporaryDirectory": "gs://bkt-df-metadata-gcp",
        "javascriptTextTransformGcsPath": "gs://bkt-df-metadata-gcp/udf.js",
        "javascriptTextTransformFunctionName": "transform"
    }