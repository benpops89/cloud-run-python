# Cloud Run with Python
This is a simple Starlette app deployed to Google Cloud Run from source code using Google Cloud Buildpacks

## Deployment
To deploy the app you need a Google Cloud Account and the gcloud SDK. When you have these you can run

`gcloud run deploy [SERVICENAME] --source . --region europe-west2 --allow-unauthenticated`

Please note the above command will mean the app is available for anyone to access, refer to the [documentation](https://cloud.google.com/sdk/gcloud/reference/run/deploy) for `gcloud run deploy` which will detail how to restrict access.
