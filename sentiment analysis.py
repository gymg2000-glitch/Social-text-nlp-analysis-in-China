import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models
import pandas as pd


data =pd.read_excel("老年人文本.xlsx",engine="openpyxl")
re=[]
for word in data["文本"]:
    txt=[]
    try:
        cred = credential.Credential(os.getenv("TENCENT_SECRET_ID"),
                             os.getenv("TENCENT_SECRET_KEY"))
        httpProfile = HttpProfile()
        httpProfile.endpoint = "nlp.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

        req = models.SentimentAnalysisRequest()
        params = {
            "Text": "{}".format(word),
            "Mode": "3class"
        }
        req.from_json_string(json.dumps(params))

        resp = client.SentimentAnalysis(req)
        print(resp.to_json_string())
        dict = resp.__dict__
        txt.append(dict["Positive"])
        txt.append(dict["Neutral"])
        txt.append(dict["Negative"])
        txt.append(dict["Sentiment"])
        re.append(txt)
    except TencentCloudSDKException as err:
        print(err)

result=pd.DataFrame(re,columns=["Positive","Neutral","Negative","Sentiment"])
result.to_excel("lao年ren.xlsx")