from prefect import task
from prefect_datafold.credentials import DatafoldCredentials

import httpx

@task
def create_diff(datafold_creds: DatafoldCredentials, payload: dict):
    """Create a Datafold diff.

    Args:
        datafold_creds (DatafoldCredentials): _description_
        payload (dict): _description_
    Example:
        Create a datafold diff for a given source and destination
        ```python
        from prefect import flow, task
        from prefect_datafold.credentials import DatafoldCredentials
        from prefect_datafold.diffs import create_diff
        
        @flow
        def flow_that_uses_datafold():
        
            datafold_creds = DatafoldCredentials.load("my-datafold-creds")
            
            diff_info = create_diff(datafold_creds, {"id": "my-dataset-id"})
            
            # do something else based on this info
        ```
    """
    headers = {
        "Authorization": f"Bearer {datafold_creds.api_key}",
        "Content-Type": "application/json"
    }
    
    # TODO: httpx.post("https://app.datafold.com/api/v1/datadiffs", ...)
    # TODO: return most actionable diff info
    pass