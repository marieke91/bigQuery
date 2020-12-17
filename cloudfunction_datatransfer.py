import time
from google.protobuf.timestamp_pb2 import Timestamp
from google.cloud import bigquery_datatransfer_v1

def runQuery (parent, requested_run_time):
    client = bigquery_datatransfer_v1.DataTransferServiceClient()
    projectid = '[enter your projectId here]' # Enter your projectID here
    transferid = '[enter your transferId here]'  # Enter your transferId here
    parent = client.project_transfer_config_path(projectid, transferid)
    start_time = bigquery_datatransfer_v1.types.Timestamp(seconds=int(time.time() + 10))
    response = client.start_manual_transfer_runs(parent, requested_run_time=start_time)
    print(response)
    
# do not forget to put google-cloud-bigquery-datatransfer==1 in the requirements.txt
