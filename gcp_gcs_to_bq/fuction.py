from googleapiclient.discovery import build
import time

def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "learning-gcp-cyb"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"
    
    # Make job name unique by adding a timestamp
    job_name = f"bq-load-gcp-{int(time.time())}"

    template_body = {
        "jobName": job_name,  # Provide a unique name for the job
        "parameters": {
        "inputFilePattern": "gs://gcp-bkt-landing-zone/user.csv",
        "JSONPath": "gs://gcp-bkt-meadata/bq.json",
        "outputTable": "learning-gcp-cyb:user_data.users",
        "bigQueryLoadingTemporaryDirectory": "gs://gcp-bkt-meadata",
        "javascriptTextTransformGcsPath": "gs://gcp-bkt-meadata/udf.js",
        "javascriptTextTransformFunctionName": "transform"
    }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)


    # Refer this youtube video for this "https://www.youtube.com/watch?v=b593huRgXic"