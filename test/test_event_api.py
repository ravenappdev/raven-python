import unittest
import json
import uuid
from raven.api import RavenClient
from raven.api_client import ApiClient
from raven.models.response import Response  
from raven.rest import RavenException


class TestEventApi(unittest.TestCase):
    """EventApi unit test stubs"""

    def setUp(self):
        try:
            file = open('/home/montooboss/Desktop/INTERN/Raven-2/raven-python/test/testData.json')
            self.testData = json.load(file)
            file.close()
            self.client = RavenClient(self.testData['apiKey'])
            self.send_testcases = self.testData['EventApi']['sendEvent']
            self.send_bulk_testcases = self.testData['EventApi']['sendBulkEvent']
        except IOError:
            raise IOError

    def tearDown(self):
        pass

    def send_bulk(self,appId=None,event=None,idempotencyKey=None,output=None):
        try:
            res = self.client.send(appId,event,idempotency_key=idempotencyKey)
            print(res)
            pass
        except RavenException as e:
            error=None
            errors=None
            if 'errors' in output:
                errors = output['errors']
            
            if 'error' in output:
                error = output['error']
            
            print(e.body)

    def send(self,appId=None,event=None,idempotencyKey=None,output=None):
        try:
            res = self.client.send(appId,event,idempotency_key=idempotencyKey)
            print(res)
            pass
        except RavenException as e:
            error=None
            errors=None
            if 'errors' in output:
                errors = output['errors']
            
            if 'error' in output:
                error = output['error']
            print(e.body)
            # exp_err = Response(error=error,errors=errors)
            # self.assertEqual(e.body,exp_err)
        
    def test_send_bulk(self):
        for test in self.send_bulk_testcases:
            input = test['input']
            output=test['output']
            name=test['name']
            appId=""
            if 'appId' in input:
                appId = input['appId']
            deserialize = ApiClient().deserialize_data
            try:
                event = deserialize(input['event'],'SendEventBulk')
                idempotencyKey = uuid.UUID.__str__(uuid.uuid4())
                self.send_bulk(appId,event,idempotencyKey,output)
            except ValueError as e:
                print(e)
            

    def test_send(self):
        for test in self.send_testcases:
            input = test['input']
            output=test['output']
            name=test['name']   
            appId=""
            if 'appId' in input:
                appId = input['appId']
            deserialize = ApiClient().deserialize_data
            try:
                event = deserialize(input['event'],'SendEvent')
                idempotencyKey = uuid.UUID.__str__(uuid.uuid4())
                self.send(appId,event,idempotencyKey,output)
            except ValueError as e:
                print(e)
            
        pass


if __name__ == '__main__':
    unittest.main()
